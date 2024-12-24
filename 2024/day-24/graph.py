from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.degree = 0
        self.visited = False


def dfs(node: Node, stack: deque[Node]) -> None:
    if node.visited:
        return
    node.visited = True
    for neighbor in node.neighbors:
        dfs(neighbor, stack)
    stack.appendleft(node)


def topological_sort(nodes: list[Node]) -> list[Node]:
    stack = deque()
    for node in nodes:
        if node.visited:
            continue
        dfs(node, stack)
    return list(stack)


