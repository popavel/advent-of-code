from functools import cache
from itertools import pairwise


@cache
def mul64(number: int) -> int:
    return number * 64


@cache
def mix(new_number: int, number: int) -> int:
    return new_number ^ number


@cache
def prune(number: int) -> int:
    return number % 16777216


@cache
def div32(number: int) -> int:
    return number // 32


def mul2048(number: int) -> int:
    return number * 2048


@cache
def calculate(number: int, num_rounds: int) -> dict[tuple[int, int, int, int], int]:
    prices = []
    curr_number = number
    for i in range(num_rounds):
        prices.append(curr_number % 10)
        curr_number = calculate_next(curr_number)

    diffs = list(pairwise(prices))
    diffs = list(map(lambda x: x[1] - x[0], diffs))

    sec_dict = {}
    for i in range(0, len(diffs) - 3, 1):
        sec = tuple(diffs[i:i + 4])
        if sec not in sec_dict:
            sec_dict[sec] = prices[i + 4]

    return sec_dict


@cache
def calculate_next(curr_number: int) -> int:
    n0 = mul64(curr_number)
    n0 = mix(n0, curr_number)
    n0 = prune(n0)
    n1 = div32(n0)
    n1 = mix(n1, n0)
    n1 = prune(n1)
    n2 = mul2048(n1)
    n2 = mix(n2, n1)
    n2 = prune(n2)
    return n2


def run(file_name: str, num_rounds: int):
    numbers = read_input(file_name)
    sequences_dicts = []
    for n in numbers:
        sequences_dicts.append(calculate(n, num_rounds))
    aggr_dict = {}
    for d in sequences_dicts:
        for k, v in d.items():
            if k not in aggr_dict:
                aggr_dict[k] = v
            else:
                aggr_dict[k] += v
    best_seq = max(aggr_dict, key=aggr_dict.get)
    print(best_seq, aggr_dict[best_seq])


def read_input(file_name):
    numbers = []
    with open(file_name, "r") as f:
        for line in f:
            numbers.append(int(line.strip()))
    return numbers


if __name__ == '__main__':
    # run("test-b1.txt", 2000)
    run("input-a.txt", 2000)
