from functools import reduce


class Node:

    def __init__(self, i, j, label):
        self.i = i
        self.j = j
        self.label = label
        self.distance = -1
        self.visited = False

    def __str__(self):
        return f'({self.i}, {self.j}), label = {self.label}, d = {self.distance}, visited = {self.visited}'

    def __repr__(self):
        return self.__str__()


def print_nodes(nodes: list[Node]):
    for n in nodes:
        print(n)


def add_cheat(cheat_nodes: list[Node], cheats: dict[int, int], distance: int):
    if len(cheat_nodes) != 1:
        raise ValueError('Invalid path')
    cheat_node = cheat_nodes[0]
    if not cheat_node.visited:
        psec = cheat_node.distance - (distance + 2)
        if psec in cheats.keys():
            cheats[psec] += 1
        else:
            cheats[psec] = 1


def read_input(file_name: str) -> list[str]:
    grid = []
    with open(file_name, 'r') as f:
        for line in f:
            grid.append(line.strip())
    return grid


def get_nodes_on_path(grid: list[str]) -> tuple[list[Node], Node, Node]:
    nodes = []
    start = None
    end = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                nodes.append(Node(i, j, '.'))
            elif grid[i][j] == 'S':
                start = Node(i, j, 'S')
                nodes.append(start)
            elif grid[i][j] == 'E':
                end = Node(i, j, 'E')
                nodes.append(end)

    if start is None:
        raise ValueError('Invalid start')
    if end is None:
        raise ValueError('Invalid end')

    return nodes, start, end


def find_distances(nodes_path: list[Node], start: Node, end: Node):
    start.distance = 0
    start.visited = True
    curr = start
    while curr != end:
        i, j = curr.i, curr.j
        nexts = [n for n in nodes_path
                 if not n.visited and (
                         (n.i == i - 1 and n.j == j)
                         or (n.i == i + 1 and n.j == j)
                         or (n.i == i and n.j == j - 1)
                         or (n.i == i and n.j == j + 1))]
        if len(nexts) != 1:
            raise ValueError('Invalid path')
        next_node = nexts[0]
        next_node.visited = True
        next_node.distance = curr.distance + 1
        curr = next_node


def unvisit(nodes: list[Node]):
    for n in nodes:
        n.visited = False


def find_cheats(nodes_path: list[Node], grid: list[str]) -> dict[int, int]:
    cheats = {}
    for n in nodes_path:
        n.visited = True
        if (n.i - 2 >= 0
                and grid[n.i - 1][n.j] == '#'
                and (grid[n.i - 2][n.j] == '.' or grid[n.i - 2][n.j] == 'E')
        ):
            cheat_nodes = list(filter(lambda cheat_n: cheat_n.i == n.i - 2 and cheat_n.j == n.j, nodes_path))
            add_cheat(cheat_nodes, cheats, n.distance)
        if (n.i + 2 < len(grid)
                and grid[n.i + 1][n.j] == '#'
                and (grid[n.i + 2][n.j] == '.' or grid[n.i + 2][n.j] == 'E')
        ):
            cheat_nodes = list(filter(lambda cheat_n: cheat_n.i == n.i + 2 and cheat_n.j == n.j, nodes_path))
            add_cheat(cheat_nodes, cheats, n.distance)
        if (n.j - 2 >= 0
                and grid[n.i][n.j - 1] == '#'
                and (grid[n.i][n.j - 2] == '.' or grid[n.i][n.j - 2] == 'E')
        ):
            cheat_nodes = list(filter(lambda cheat_n: cheat_n.i == n.i and cheat_n.j == n.j - 2, nodes_path))
            add_cheat(cheat_nodes, cheats, n.distance)
        if (n.j + 2 < len(grid[n.i])
                and grid[n.i][n.j + 1] == '#'
                and (grid[n.i][n.j + 2] == '.' or grid[n.i][n.j + 2] == 'E')
        ):
            cheat_nodes = list(filter(lambda cheat_n: cheat_n.i == n.i and cheat_n.j == n.j + 2, nodes_path))
            add_cheat(cheat_nodes, cheats, n.distance)

    return cheats


def find_useful_cheats(cheats: list[tuple[int, int]], threshold: int) -> list[tuple[int, int]]:
    return [c for c in cheats if c[0] >= threshold]


def compute_useful_cheats(useful_cheats: list[tuple[int, int]]) -> int:
    return reduce(lambda x, y: x + y[1], useful_cheats, 0)


def run():
    grid = read_input("input-a.txt")

    nodes_path, start, end = get_nodes_on_path(grid)
    find_distances(nodes_path, start, end)
    nodes_path = sorted(nodes_path, key=lambda n: n.distance)

    print("Nodes path")
    print(nodes_path)
    print(len(nodes_path))

    unvisit(nodes_path)

    cheats = find_cheats(nodes_path, grid)
    cheats = sorted(cheats.items(), key=lambda x: x[0])

    print("Cheats")
    print(cheats)

    useful_cheats = find_useful_cheats(cheats, 100)
    num_useful_cheats = compute_useful_cheats(useful_cheats)

    print("Useful cheats")
    print(useful_cheats)
    print(num_useful_cheats)


if __name__ == '__main__':
    run()
