from collections import deque


num_sequences = {}
dir_sequences = {}


class Node:
    def __init__(self, value):
        self.value = value
        self.i = -1
        self.j = -1
        self.parents = []
        self.neighbors = []
        self.visited = False
        self.distance = -1

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


def create_graph_num() -> list[Node]:
    graph_num = []
    for i in range(10):
        graph_num.append(Node(i))
    graph_num.append(Node('A'))

    graph_num[0].neighbors.append((graph_num[-1], '>'))
    graph_num[0].neighbors.append((graph_num[2], '^'))
    graph_num[0].i = 3
    graph_num[0].j = 1

    graph_num[1].neighbors.append((graph_num[2], '>'))
    graph_num[1].neighbors.append((graph_num[4], '^'))
    graph_num[1].i = 2
    graph_num[1].j = 0

    graph_num[2].neighbors.append((graph_num[0], 'v'))
    graph_num[2].neighbors.append((graph_num[1], '<'))
    graph_num[2].neighbors.append((graph_num[3], '>'))
    graph_num[2].neighbors.append((graph_num[5], '^'))
    graph_num[2].i = 2
    graph_num[2].j = 1

    graph_num[3].neighbors.append((graph_num[-1], 'v'))
    graph_num[3].neighbors.append((graph_num[2], '<'))
    graph_num[3].neighbors.append((graph_num[6], '^'))
    graph_num[3].i = 2
    graph_num[3].j = 2

    graph_num[4].neighbors.append((graph_num[1], 'v'))
    graph_num[4].neighbors.append((graph_num[5], '>'))
    graph_num[4].neighbors.append((graph_num[7], '^'))
    graph_num[4].i = 1
    graph_num[4].j = 0

    graph_num[5].neighbors.append((graph_num[2], 'v'))
    graph_num[5].neighbors.append((graph_num[4], '<'))
    graph_num[5].neighbors.append((graph_num[6], '>'))
    graph_num[5].neighbors.append((graph_num[8], '^'))
    graph_num[5].i = 1
    graph_num[5].j = 1

    graph_num[6].neighbors.append((graph_num[3], 'v'))
    graph_num[6].neighbors.append((graph_num[5], '<'))
    graph_num[6].neighbors.append((graph_num[9], '^'))
    graph_num[6].i = 1
    graph_num[6].j = 2

    graph_num[7].neighbors.append((graph_num[4], 'v'))
    graph_num[7].neighbors.append((graph_num[8], '>'))
    graph_num[7].i = 0
    graph_num[7].j = 0

    graph_num[8].neighbors.append((graph_num[5], 'v'))
    graph_num[8].neighbors.append((graph_num[7], '<'))
    graph_num[8].neighbors.append((graph_num[9], '>'))
    graph_num[8].i = 0
    graph_num[8].j = 1

    graph_num[9].neighbors.append((graph_num[6], 'v'))
    graph_num[9].neighbors.append((graph_num[8], '<'))
    graph_num[9].i = 0
    graph_num[9].j = 2

    graph_num[10].neighbors.append((graph_num[0], '<'))
    graph_num[10].neighbors.append((graph_num[3], '^'))
    graph_num[10].i = 3
    graph_num[10].j = 2

    return graph_num


def get_seq_from_parent(p: Node, start: Node) -> list[str]:
    if p == start:
        return ['']
    else:
        sequences = []
        for parent, direction in p.parents:
            ss = get_seq_from_parent(parent, start)
            for s in ss:
                sequences.append(direction + s)
        return sequences


def get_shortest_sequences_for_char(chars: str, graph_num: list[Node]) -> list[str]:
    if chars in num_sequences.keys():
        return num_sequences[chars]

    for n in graph_num:
        n.visited = False
        n.distance = -1
        n.parents = []

    start = graph_num[len(graph_num) - 1] if chars[0] == 'A' else graph_num[int(chars[0])]
    end = graph_num[len(graph_num) - 1] if chars[1] == 'A' else graph_num[int(chars[1])]

    bfs(start, end)
    sequences = get_sequences(start, end)

    num_sequences[chars] = sequences

    return sequences


def create_graph_dir() -> list[Node]:
    graph_dir = []
    for c in ['^', '>', 'v', '<', 'A']:
        graph_dir.append(Node(c))

    graph_dir[0].neighbors.append((graph_dir[2], 'v'))
    graph_dir[0].neighbors.append((graph_dir[4], '>'))

    graph_dir[1].neighbors.append((graph_dir[2], '<'))
    graph_dir[1].neighbors.append((graph_dir[4], '^'))

    graph_dir[2].neighbors.append((graph_dir[0], '^'))
    graph_dir[2].neighbors.append((graph_dir[1], '>'))
    graph_dir[2].neighbors.append((graph_dir[3], '<'))

    graph_dir[3].neighbors.append((graph_dir[2], '>'))

    graph_dir[4].neighbors.append((graph_dir[0], '<'))
    graph_dir[4].neighbors.append((graph_dir[1], 'v'))

    return graph_dir


def get_shortest_seqs_for_dir(dirs: tuple[str, str], graph_dir: list[Node]) -> list[str]:
    if dirs in dir_sequences.keys():
        return dir_sequences[dirs]

    for n in graph_dir:
        n.visited = False
        n.distance = -1
        n.parents = []

    start = None
    match dirs[0]:
        case '^':
            start = graph_dir[0]
        case '>':
            start = graph_dir[1]
        case 'v':
            start = graph_dir[2]
        case '<':
            start = graph_dir[3]
        case 'A':
            start = graph_dir[4]

    end = None
    match dirs[1]:
        case '^':
            end = graph_dir[0]
        case '>':
            end = graph_dir[1]
        case 'v':
            end = graph_dir[2]
        case '<':
            end = graph_dir[3]
        case 'A':
            end = graph_dir[4]

    bfs(start, end)
    sequences = get_sequences(start, end)

    dir_sequences[dirs] = sequences

    return sequences


def get_sequences(start, end):
    if start == end:
        return ['A']

    sequences = []
    for p, direction in end.parents:
        ss = get_seq_from_parent(p, start)
        for seq in ss:
            sequences.append(('A' + direction + seq)[::-1])
    return sequences


def bfs(start: Node, end: Node):
    start.distance = 0
    start.visited = True
    q = deque()
    q.append(start)
    while len(q) > 0:
        n = q.popleft()
        if n == end:
            break

        for neighbor, direction in n.neighbors:
            if not neighbor.visited:
                neighbor.visited = True
                neighbor.distance = n.distance + 1
                neighbor.parents.append((n, direction))
                q.append(neighbor)
            elif neighbor.distance == n.distance + 1:
                neighbor.parents.append((n, direction))
