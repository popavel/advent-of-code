import math
from collections import deque


class Node:
    def __init__(self, i, j, label):
        self.coordinates = (i, j)
        self.label = label
        self.visited = False
        self.distance = math.inf
        self.direction = None
        self.neighbours = []
        self.parents = []

    def __str__(self):
        return f'({self.coordinates}, {self.label}, {self.distance}, neighbours: {[n.coordinates for n in self.neighbours]}, parents: {[n.coordinates for n in self.parents]}\n'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    grid = []
    with open('input-a.txt', 'r') as f:
        for line in f:
            grid += [line.strip()]

    # print('\n'.join(grid))

    graph = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                row += [Node(i, j, 'n')]
            elif grid[i][j] == 'S':
                row += [Node(i, j, 's')]
            elif grid[i][j] == 'E':
                row += [Node(i, j, 'e')]
            elif grid[i][j] == '#':
                row += [Node(i, j, '#')]
            else:
                raise Exception('Invalid grid character.')
        graph += [row]

    # print(graph)

    s = None
    e = None
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j].label == '#':
                continue
            else:
                if graph[i + 1][j].label != '#':
                    graph[i][j].neighbours += [graph[i + 1][j]]
                if graph[i - 1][j].label != '#':
                    graph[i][j].neighbours += [graph[i - 1][j]]
                if graph[i][j + 1].label != '#':
                    graph[i][j].neighbours += [graph[i][j + 1]]
                if graph[i][j - 1].label != '#':
                    graph[i][j].neighbours += [graph[i][j - 1]]
            if graph[i][j].label == 's':
                s = graph[i][j]
            elif graph[i][j].label == 'e':
                e = graph[i][j]

    # print(s)
    # print(e)
    # print(graph)

    q = deque()
    s.distance = 0
    s.direction = 'e'
    q.append(s)
    while len(q) > 0:
        current = min(q, key=lambda x: x.distance)
        q.remove(current)
        current.visited = True
        for n in current.neighbours:
            if not n.visited:
                cost = None
                new_direction = None
                if current.direction == 'e':
                    if n.coordinates[1] == current.coordinates[1] + 1:
                        cost = 1
                        new_direction = 'e'
                    elif n.coordinates[1] == current.coordinates[1] - 1:
                        cost = 2001
                        new_direction = 'w'
                    elif n.coordinates[0] == current.coordinates[0] + 1:
                        cost = 1001
                        new_direction = 's'
                    elif n.coordinates[0] == current.coordinates[0] - 1:
                        cost = 1001
                        new_direction = 'n'
                elif current.direction == 'w':
                    if n.coordinates[1] == current.coordinates[1] + 1:
                        cost = 2001
                        new_direction = 'e'
                    elif n.coordinates[1] == current.coordinates[1] - 1:
                        cost = 1
                        new_direction = 'w'
                    elif n.coordinates[0] == current.coordinates[0] + 1:
                        cost = 1001
                        new_direction = 's'
                    elif n.coordinates[0] == current.coordinates[0] - 1:
                        cost = 1001
                        new_direction = 'n'
                elif current.direction == 'n':
                    if n.coordinates[1] == current.coordinates[1] + 1:
                        cost = 1001
                        new_direction = 'e'
                    elif n.coordinates[1] == current.coordinates[1] - 1:
                        cost = 1001
                        new_direction = 'w'
                    elif n.coordinates[0] == current.coordinates[0] + 1:
                        cost = 2001
                        new_direction = 's'
                    elif n.coordinates[0] == current.coordinates[0] - 1:
                        cost = 1
                        new_direction = 'n'
                elif current.direction == 's':
                    if n.coordinates[1] == current.coordinates[1] + 1:
                        cost = 1001
                        new_direction = 'e'
                    elif n.coordinates[1] == current.coordinates[1] - 1:
                        cost = 1001
                        new_direction = 'w'
                    elif n.coordinates[0] == current.coordinates[0] + 1:
                        cost = 1
                        new_direction = 's'
                    elif n.coordinates[0] == current.coordinates[0] - 1:
                        cost = 2001
                        new_direction = 'n'
                if cost is None:
                    raise Exception('Invalid cost.')
                if new_direction is None:
                    raise Exception('Invalid direction.')
                if n.distance > cost + current.distance:
                    n.distance = cost + current.distance
                    n.direction = new_direction
                    n.parents += [current]
                if n not in q:
                    q.append(n)

    print(e.distance)
    # print(e)
    # next_node = e.parents[0]
    # while next_node.label != 's':
    #     print(next_node)
    #     next_node = next_node.parents[0]
    # print(next_node)
