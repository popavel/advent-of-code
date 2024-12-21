from functools import cache
from itertools import pairwise

import graphs


def split_on_a(seq: str) -> list[str]:
    split = []

    idx_start = 0
    for i, c in enumerate(seq):
        if c == 'A':
            split.append(seq[idx_start:i + 1])
            idx_start = i + 1

    return split


@cache
def find_shortest_seq(sequence: str, depth: int) -> int:
    # if (sequence, depth) in memo_dict.keys():
    #     return memo_dict[(sequence, depth)]

    res = 0
    sequence = 'A' + sequence
    for dirs in pairwise(sequence):
        new_sequences = graphs.get_shortest_seqs_for_dir(dirs, graph_dir)
        if depth == 0:
            res += min(len(s) for s in new_sequences)
        else:
            lengths = []
            for s in new_sequences:
                new_length = find_shortest_seq(s, depth - 1)
                lengths.append(new_length)
            res += min(lengths)

    # memo_dict[(sequence, depth)] = res
    return res


def find_shortest_seq_length(seqs: list[str]) -> int:
    sss = []

    for s in seqs:
        ss = find_shortest_seq(s, 24)
        sss.append(ss)
    return min(sss)


def find_shortest_sequence_for_code(code: str) -> int:
    s = 0

    for i in range(-1, 3):
        chars = code[i] + code[i + 1]
        ssc = graphs.get_shortest_sequences_for_char(chars, graph_num)
        seq_length = find_shortest_seq_length(ssc)
        print(chars)
        print(ssc)
        print(seq_length)

        s += seq_length

    return s


def run(input_codes: list[str]):
    shortest_sequences = {}
    for code in input_codes:
        shortest_sequences[code] = find_shortest_sequence_for_code(code)

    print(shortest_sequences)

    complexities = []
    for key, value in shortest_sequences.items():
        complexities.append(int(key[:3]) * value)

    print(complexities)
    print(sum(complexities))


if __name__ == '__main__':
    graph_num = graphs.create_graph_num()
    graph_dir = graphs.create_graph_dir()

    memo_dict = {}

    test = ['029A', '980A', '179A', '456A', '379A']
    inp = ['839A', '169A', '579A', '670A', '638A']
    run(inp)
