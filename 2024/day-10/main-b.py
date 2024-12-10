from collections import deque


class Node:

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.neighbours = []
        self.visited = False

    def __str__(self):
        return f'({self.x}, {self.y}) - {self.value}, neighbours: {[(n.x, n.y) for n in self.neighbours]}\n'

    def __repr__(self):
        return self.__str__()


def create_dag(grid):
    nodes = []
    for i in range(len(grid)):
        nodes_row = []
        for j in range(len(grid[0])):
            nodes_row.append(Node(i, j, grid[i][j]))
        nodes.append(nodes_row)

    for row in nodes:
        for n in row:
            i = n.x
            j = n.y
            v = n.value
            neighbours = []
            if 0 < i < len(grid) - 1 and 0 < j < len(grid[0]) - 1:
                if nodes[i - 1][j].value == v + 1:
                    neighbours.append(nodes[i - 1][j])
                if nodes[i + 1][j].value == v + 1:
                    neighbours.append(nodes[i + 1][j])
                if nodes[i][j - 1].value == v + 1:
                    neighbours.append(nodes[i][j - 1])
                if nodes[i][j + 1].value == v + 1:
                    neighbours.append(nodes[i][j + 1])
            elif i == 0 and 0 < j < len(grid[0]) - 1:
                if nodes[i + 1][j].value == v + 1:
                    neighbours.append(nodes[i + 1][j])
                if nodes[i][j - 1].value == v + 1:
                    neighbours.append(nodes[i][j - 1])
                if nodes[i][j + 1].value == v + 1:
                    neighbours.append(nodes[i][j + 1])
            elif i == len(grid) - 1 and 0 < j < len(grid[0]) - 1:
                if nodes[i - 1][j].value == v + 1:
                    neighbours.append(nodes[i - 1][j])
                if nodes[i][j - 1].value == v + 1:
                    neighbours.append(nodes[i][j - 1])
                if nodes[i][j + 1].value == v + 1:
                    neighbours.append(nodes[i][j + 1])
            elif 0 < i < len(grid) - 1 and j == 0:
                if nodes[i - 1][j].value == v + 1:
                    neighbours.append(nodes[i - 1][j])
                if nodes[i + 1][j].value == v + 1:
                    neighbours.append(nodes[i + 1][j])
                if nodes[i][j + 1].value == v + 1:
                    neighbours.append(nodes[i][j + 1])
            elif 0 < i < len(grid) - 1 and j == len(grid[0]) - 1:
                if nodes[i - 1][j].value == v + 1:
                    neighbours.append(nodes[i - 1][j])
                if nodes[i + 1][j].value == v + 1:
                    neighbours.append(nodes[i + 1][j])
                if nodes[i][j - 1].value == v + 1:
                    neighbours.append(nodes[i][j - 1])
            elif i == 0 and j == 0:
                if nodes[i + 1][j].value == v + 1:
                    neighbours.append(nodes[i + 1][j])
                if nodes[i][j + 1].value == v + 1:
                    neighbours.append(nodes[i][j + 1])
            elif i == 0 and j == len(grid[0]) - 1:
                if nodes[i + 1][j].value == v + 1:
                    neighbours.append(nodes[i + 1][j])
                if nodes[i][j - 1].value == v + 1:
                    neighbours.append(nodes[i][j - 1])
            elif i == len(grid) - 1 and j == 0:
                if nodes[i - 1][j].value == v + 1:
                    neighbours.append(nodes[i - 1][j])
                if nodes[i][j + 1].value == v + 1:
                    neighbours.append(nodes[i][j + 1])
            elif i == len(grid) - 1 and j == len(grid[0]) - 1:
                if nodes[i - 1][j].value == v + 1:
                    neighbours.append(nodes[i - 1][j])
                if nodes[i][j - 1].value == v + 1:
                    neighbours.append(nodes[i][j - 1])
            n.neighbours = neighbours
    return nodes


def bfs(node):
    reachable = []
    reachable.append(node)
    nexts = deque()
    for n in node.neighbours:
        nexts.append(n)
    while len(nexts) > 0:
        n = nexts.pop()
        reachable.append(n)
        for nn in n.neighbours:
            nexts.append(nn)

    count = 0
    for n in reachable:
        if n.value == 9:
            count += 1

    return count


if __name__ == '__main__':
    grid = []
    with open('input-a.txt', 'r') as f:
        for line in f:
            input_line = line.strip()
            grid.append([int(c) for c in input_line])

    dag = create_dag(grid)

    starting_nodes = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if dag[i][j].value == 0:
                starting_nodes.append(dag[i][j])

    scores = []
    for n in starting_nodes:
        scores.append(bfs(n))

    print(scores)
    print(sum(scores))
