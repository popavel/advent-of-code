from collections import deque
from functools import reduce


class Node:

    def __init__(self, i, j, label):
        self.i = i
        self.j = j
        self.label = label
        self.distance = -1
        self.bfs_distance = -1
        self.visited = False
        self.neighbours = []

    def __str__(self):
        return f'({self.i}, {self.j}), label = {self.label}, d = {self.distance}, visited = {self.visited}, neighbours = {[(n.i, n.j) for n in self.neighbours]}'

    def __repr__(self):
        return self.__str__()


def print_nodes(nodes: list[Node]):
    for n in nodes:
        print(n)


def add_cheats(node: Node, nodes_grid: list[list[Node]], cheats: dict[int, int]):
    for i in range(max(0, node.i - 20), min(len(nodes_grid), node.i + 21)):
        for j in range(max(0, node.j - 20), min(len(nodes_grid[i]), node.j + 21)):
            if nodes_grid[i][j].label != '#' and -1 < nodes_grid[i][j].bfs_distance <= 20:
                psec = nodes_grid[i][j].distance - (node.distance + nodes_grid[i][j].bfs_distance)
                if psec <= 0:
                    continue
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


def get_nodes_on_path(nodes_grid: list[list[Node]]) -> tuple[list[Node], Node, Node]:
    nodes_path: list[Node] = []
    start = None
    end = None
    for i in range(len(nodes_grid)):
        for j in range(len(nodes_grid[i])):
            if nodes_grid[i][j].label == '.':
                nodes_path.append(nodes_grid[i][j])
            elif nodes_grid[i][j].label == 'S':
                start = nodes_grid[i][j]
                nodes_path.append(start)
            elif nodes_grid[i][j].label == 'E':
                end = nodes_grid[i][j]
                nodes_path.append(end)

    if start is None:
        raise ValueError('Invalid start')
    if end is None:
        raise ValueError('Invalid end')

    return nodes_path, start, end


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


def unvisit_nodes(nodes: list[Node]):
    for n in nodes:
        n.visited = False


def find_closest_nodes(n: Node, nodes_path: list[Node]) -> list[Node]:
    nodes_in_proximity = []
    for node in nodes_path:
        if abs(n.i - node.i) + abs(n.j - node.j) <= 20 and not node.visited:
            nodes_in_proximity.append(node)
    return nodes_in_proximity


def make_neighbour(node: Node, nodes_grid: list[list[Node]]):
    i, j = node.i, node.j
    if nodes_grid[i - 1][j].label == '#':
        node.neighbours.append(nodes_grid[i - 1][j])
        nodes_grid[i - 1][j].neighbours.append(node)
    if nodes_grid[i + 1][j].label == '#':
        node.neighbours.append(nodes_grid[i + 1][j])
        nodes_grid[i + 1][j].neighbours.append(node)
    if nodes_grid[i][j - 1].label == '#':
        node.neighbours.append(nodes_grid[i][j - 1])
        nodes_grid[i][j - 1].neighbours.append(node)
    if nodes_grid[i][j + 1].label == '#':
        node.neighbours.append(nodes_grid[i][j + 1])
        nodes_grid[i][j + 1].neighbours.append(node)


def unmake_neighbour(node: Node, nodes_grid: list[list[Node]]):
    i, j = node.i, node.j
    if nodes_grid[i - 1][j].label == '#':
        nodes_grid[i - 1][j].neighbours.remove(node)
    if nodes_grid[i + 1][j].label == '#':
        nodes_grid[i + 1][j].neighbours.remove(node)
    if nodes_grid[i][j - 1].label == '#':
        nodes_grid[i][j - 1].neighbours.remove(node)
    if nodes_grid[i][j + 1].label == '#':
        nodes_grid[i][j + 1].neighbours.remove(node)
    node.neighbours = []


def unvisit_node_grid(node: Node, nodes_grid: list[list[Node]]):
    for i in range(max(0, node.i - 20), min(len(nodes_grid), node.i + 21)):
        for j in range(max(0, node.j - 20), min(len(nodes_grid[i]), node.j + 21)):
            nodes_grid[i][j].visited = False
            nodes_grid[i][j].bfs_distance = -1


def bfs(start: Node):
    start.bfs_distance = 0
    start.visited = True
    q = deque()
    q.append(start)
    while len(q) > 0:
        curr = q.popleft()
        for n in curr.neighbours:
            if not n.visited:
                if curr.bfs_distance + 1 <= 20:
                    n.visited = True
                    n.bfs_distance = curr.bfs_distance + 1
                    q.append(n)


def find_cheats(nodes_path: list[Node], nodes_grid: list[list[Node]]) -> dict[int, int]:
    cheats = {}
    for n in nodes_path:
        bfs(n)
        add_cheats(n, nodes_grid, cheats)
        unvisit_node_grid(n, nodes_grid)

    return cheats


def find_useful_cheats(cheats: list[tuple[int, int]], threshold: int) -> list[tuple[int, int]]:
    return [c for c in cheats if c[0] >= threshold]


def compute__num_useful_cheats(useful_cheats: list[tuple[int, int]]) -> int:
    return reduce(lambda x, y: x + y[1], useful_cheats, 0)


def get_nodes_grid(grid: list[str]) -> list[list[Node]]:
    nodes_grid = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[i])):
            row.append(Node(i, j, grid[i][j]))
        nodes_grid.append(row)

    for i in range(len(nodes_grid)):
        for j in range(len(nodes_grid[i])):
            n = nodes_grid[i][j]
            if i - 1 >= 0:
                n.neighbours.append(nodes_grid[i - 1][j])
            if i + 1 < len(nodes_grid):
                n.neighbours.append(nodes_grid[i + 1][j])
            if j - 1 >= 0:
                n.neighbours.append(nodes_grid[i][j - 1])
            if j + 1 < len(nodes_grid[i]):
                n.neighbours.append(nodes_grid[i][j + 1])

    return nodes_grid


def run():
    grid = read_input("input-a.txt")

    nodes_grid = get_nodes_grid(grid)
    nodes_path, start, end = get_nodes_on_path(nodes_grid)
    find_distances(nodes_path, start, end)
    nodes_path = sorted(nodes_path, key=lambda n: n.distance)

    print("Nodes path")
    print(nodes_path)
    print(len(nodes_path))

    unvisit_nodes(nodes_path)

    cheats = find_cheats(nodes_path, nodes_grid)
    cheats = sorted(cheats.items(), key=lambda x: x[0])

    print("Cheats")
    print(cheats)

    useful_cheats = find_useful_cheats(cheats, 100)
    num_useful_cheats = compute__num_useful_cheats(useful_cheats)

    print("Useful cheats")
    print(useful_cheats)
    print(num_useful_cheats)


if __name__ == '__main__':
    run()
