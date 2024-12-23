from itertools import combinations


def is_clique3(c: tuple[int, int, int]) -> bool:
    return edges_matrix[c[0]][c[1]] == 1 and edges_matrix[c[1]][c[2]] == 1 and edges_matrix[c[0]][c[2]] == 1


def is_clique(c: tuple[int, ...], new_value: int) -> bool:
    for v in c:
        if edges_matrix[v][new_value] == 0:
            return False
    return True


def run():
    possible_cliques_3 = list(combinations(vertices_as_int, 3))
    cliques_3 = [c for c in possible_cliques_3 if is_clique3(tuple(sorted(c)))]

    cliques_curr = {}
    for c in cliques_3:
        cliques_curr[c] = 1

    # vs_in_cliques = set()
    # for c in cliques_curr:
    #     for v in c:
    #         vs_in_cliques.add(v)

    while True:
        print(len(cliques_curr))
        cliques_next = {}
        for c in cliques_curr:
            # for v in vs_in_cliques:
            for v in vertices_as_int:
                # if v not in c and cliques_next.get(tuple(sorted(list(c) + [v]))) is None:
                if v not in c:
                    if is_clique(c, v):
                        c_new = tuple(sorted(list(c) + [v]))
                        cliques_next[c_new] = 1
        if not cliques_next:
            break
        cliques_curr = cliques_next.copy()
        # vs_in_cliques = set()
        # for c in cliques_curr:
        #     for v in c:
        #         vs_in_cliques.add(v)

    print(cliques_curr)
    clueques_text = [vertices[c] for c in list(cliques_curr)[0]]
    print(','.join(clueques_text))


def read_input(file_name: str) -> list[list[str]]:
    edges = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip().split('-')
            if line:
                edges.append(sorted((line[0], line[1])))
    return edges


if __name__ == '__main__':
    # edges = read_input("test-a.txt")
    edges = read_input("input-a.txt")
    print(len(edges))

    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    vertices = sorted(list(vertices))
    print(len(vertices))
    edges_matrix = [[0] * len(vertices) for _ in range(len(vertices))]
    for edge in edges:
        i = vertices.index(edge[0])
        j = vertices.index(edge[1])
        edges_matrix[i][j] = 1
        edges_matrix[j][i] = 1

    vertices_as_int = [i for i in range(len(vertices))]

    # run()
    run()
