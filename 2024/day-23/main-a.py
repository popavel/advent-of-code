from itertools import combinations


def is_clique(c: tuple[int, int, int], edge_matrix: list[list[int]]) -> bool:
    return edge_matrix[c[0]][c[1]] == 1 and edge_matrix[c[1]][c[2]] == 1 and edge_matrix[c[0]][c[2]] == 1


def run(file_name: str):
    edges = read_input(file_name)
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
    possible_cliques = list(combinations(vertices_as_int, 3))
    print(len(possible_cliques))

    cliques_3 = [c for c in possible_cliques if is_clique(c, edges_matrix)]
    print(len(cliques_3))
    cliques_3 = [c for c in cliques_3 if vertices[c[0]][0] == 't' or vertices[c[1]][0] == 't' or vertices[c[2]][0] == 't']
    print(cliques_3)
    print(len(cliques_3))


def read_input(file_name: str) -> list[list[str]]:
    edges = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip().split('-')
            if line:
                edges.append(sorted((line[0], line[1])))
    return edges


if __name__ == '__main__':
    # run("test-a.txt")
    run("input-a.txt")
