import graphs


def find_shortest_sequences(seqs: list[str]) -> list[str]:
    curr_sequences = seqs.copy()
    for robot in range(2):
        next_sequences = []
        for seq in curr_sequences:
            s = []
            for i, c in enumerate(seq):
                if i == 0:
                    dirs = 'A' + c
                else:
                    dirs = seq[i - 1] + c

                if dirs in known_sequences[robot].keys():
                    new_sequences = known_sequences[robot][dirs]
                else:
                    new_sequences = graphs.get_shortest_seqs_for_dir(dirs, graph_dir)
                    known_sequences[robot][dirs] = new_sequences
                if len(s) == 0:
                    s = new_sequences.copy()
                else:
                    s = [ss + ns for ss in s for ns in new_sequences]
            next_sequences.extend(s)
        curr_sequences = next_sequences.copy()

    return curr_sequences


def find_shortest_sequence_for_code(code: str) -> str:
    s = ''

    for i in range(-1, 3):
        chars = code[i] + code[i + 1]
        ssc = graphs.get_shortest_sequences_for_char(chars, graph_num)
        ss = find_shortest_sequences(ssc)
        print(chars)
        print(ssc)
        print(ss)

        shortest_sequence = ss[0]
        for sss in ss:
            if len(sss) < len(shortest_sequence):
                shortest_sequence = sss
        s += shortest_sequence

    return s


def run(input_codes: list[str]):
    shortest_sequences = {}
    for code in input_codes:
        shortest_sequences[code] = find_shortest_sequence_for_code(code)

    print(shortest_sequences)

    complexities = []
    for key, value in shortest_sequences.items():
        complexities.append((int(key[:3]), len(value)))
    print(complexities)

    print(list(map(lambda x: x[0] * x[1], complexities)))
    print(sum(list(map(lambda x: x[0] * x[1], complexities))))


if __name__ == '__main__':
    graph_num = graphs.create_graph_num()
    graph_dir = graphs.create_graph_dir()

    known_sequences = [{}, {}, {}]

    test = ['029A', '980A', '179A', '456A', '379A']
    inp = ['839A', '169A', '579A', '670A', '638A']
    run(inp)
