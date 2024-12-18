from collections import deque


class Node:

    def __init__(self, i, j, value):
        self.i = i
        self.j = j
        self.value = value
        self.distance = -1
        self.neighbours = []
        self.visited = False

    def __str__(self):
        return f'({self.i}, {self.j}) , neighbours: {[(n.i, n.j) for n in self.neighbours]}\n'

    def __repr__(self):
        return self.__str__()



if __name__ == '__main__':
    dim_test = 7
    dim_input = 71
    steps_test = 12
    steps_input = 1024

    b = []
    with open('test-a.txt', 'r') as f:
        for line in f:
            line = list(map(int, line.strip().split(',')))
            b.append((line[0], line[1]))

    m = n = dim_test
    steps = steps_test

    grid = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(steps):
        x, y = b[i]
        grid[y][x] = 1

    nodes = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(Node(i, j, grid[i][j]))
        nodes.append(row)

    for i in range(m):
        for j in range(n):
            if nodes[i][j].value == 1:
                continue
            if 0 < i < m-1 and 0 < j < n-1:
                if nodes[i-1][j].value != 1:
                    nodes[i][j].neighbours.append(nodes[i-1][j])
                if nodes[i+1][j].value != 1:
                    nodes[i][j].neighbours.append(nodes[i+1][j])
                if nodes[i][j-1].value != 1:
                    nodes[i][j].neighbours.append(nodes[i][j-1])
                if nodes[i][j+1].value != 1:
                    nodes[i][j].neighbours.append(nodes[i][j+1])
            elif i == 0 and j == 0:
                if nodes[i+1][j].value != 1:
                    nodes[i][j].neighbours.append(nodes[i+1][j])
                if nodes[i][j+1].value != 1:
                    nodes[i][j].neighbours.append(nodes[i][j+1])
            elif i == 0 and j == n-1:
                if nodes[i+1][j].value != 1:
                    nodes[i][j].neighbours.append(nodes[i+1][j])
                if nodes[i][j-1].value != 1:
                    nodes[i][j].neighbours.append(nodes[i][j-1])
            elif i == m-1 and j == 0:
                if nodes[i-1][j].value != 1:
                    nodes[i][j].neighbours.append(nodes[i-1][j])
                if nodes[i][j+1].value != 1:
                    nodes[i][j].neighbours.append(nodes[i][j+1])
            elif i == m-1 and j == n-1:
                if nodes[i-1][j].value != 1:
                    nodes[i][j].neighbours.append(nodes[i-1][j])
                if nodes[i][j-1].value != 1:
                    nodes[i][j].neighbours.append(nodes[i][j-1])
            elif i == 0 and 0 < j < n-1:
                if nodes[i+1][j].value != 1:
                    nodes[i][j].neighbours.append(nodes[i+1][j])
                if nodes[i][j-1].value != 1:
                    nodes[i][j].neighbours.append(nodes[i][j-1])
                if nodes[i][j+1].value != 1:
                    nodes[i][j].neighbours.append(nodes[i][j+1])
            elif i == m-1 and 0 < j < n-1:
                if nodes[i-1][j].value != 1:
                    nodes[i][j].neighbours.append(nodes[i-1][j])
                if nodes[i][j-1].value != 1:
                    nodes[i][j].neighbours.append(nodes[i][j-1])
                if nodes[i][j+1].value != 1:
                    nodes[i][j].neighbours.append(nodes[i][j+1])
            elif 0 < i < m-1 and j == 0:
                if nodes[i-1][j].value != 1:
                    nodes[i][j].neighbours.append(nodes[i-1][j])
                if nodes[i+1][j].value != 1:
                    nodes[i][j].neighbours.append(nodes[i+1][j])
                if nodes[i][j+1].value != 1:
                    nodes[i][j].neighbours.append(nodes[i][j+1])
            elif 0 < i < m-1 and j == n-1:
                if nodes[i-1][j].value != 1:
                    nodes[i][j].neighbours.append(nodes[i-1][j])
                if nodes[i+1][j].value != 1:
                    nodes[i][j].neighbours.append(nodes[i+1][j])
                if nodes[i][j-1].value != 1:
                    nodes[i][j].neighbours.append(nodes[i][j-1])

    s = nodes[0][0]
    e = nodes[m-1][n-1]

    s.distance = 0
    s.visited = True
    q = deque()
    q.append(s)
    while len(q) > 0:
        node = q.popleft()
        if node == e:
            print(node.distance)
            break
        for neighbour in node.neighbours:
            if not neighbour.visited:
                neighbour.visited = True
                neighbour.distance = node.distance + 1
                q.append(neighbour)