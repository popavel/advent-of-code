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


def find_distance(s, e):
    q = deque()
    s.distance = 0
    q.append(s)
    while len(q) > 0:
        current = min(q, key=lambda x: x.distance)
        q.remove(current)
        current.visited = True
        if current == e:
            break
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
    return e.distance


def initialize_graph(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j].visited = False
            graph[i][j].distance = math.inf
            graph[i][j].direction = None
            graph[i][j].parents = []


if __name__ == '__main__':
    # a much more efficient way would be to remove any node that requires a turn.
    #  Example:
    #   ######
    #   #de
    #   #c##
    #   #ab
    #   ######
    # Remove the nodes a and d and define edges between b and c and c and e.
    # If a == S, do not remove it, but directly define the corresponding edge cost. Same for a == E.
    grid = []
    with open('input-a.txt', 'r') as f:
        for line in f:
            grid += [line.strip()]
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

    initialize_graph(graph)

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

    s.direction = 'e'
    min_distance = find_distance(s, e)
    seats = []
    curr_node = e
    while curr_node != s:
        seats += [curr_node.coordinates]
        curr_node = curr_node.parents[0]
    seats += [s.coordinates]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            n = graph[i][j]
            if n.coordinates not in seats:
                possible_seats = []
                initialize_graph(graph)
                s.direction = 'e'
                d0 = find_distance(s, n)
                curr_node = n
                while curr_node != s and len(curr_node.parents) > 0:
                    possible_seats += [curr_node.coordinates]
                    curr_node = curr_node.parents[0]
                direction = n.direction
                initialize_graph(graph)
                n.direction = direction
                d1 = find_distance(n, e)
                curr_node = e
                while curr_node != n and len(curr_node.parents) > 0:
                    possible_seats += [curr_node.coordinates]
                    curr_node = curr_node.parents[0]
                if d0 + d1 == min_distance:
                    for seat in possible_seats:
                        if seat not in seats:
                            seats += [seat]
    print(len(seats))
    print(seats)
    print(min_distance)