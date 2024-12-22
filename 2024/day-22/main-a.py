from functools import cache


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
def calculate(number: int, num_rounds: int) -> int:
    curr_number = number
    for i in range(num_rounds):
        n0 = mul64(curr_number)
        n0 = mix(n0, curr_number)
        n0 = prune(n0)

        n1 = div32(n0)
        n1 = mix(n1, n0)
        n1 = prune(n1)

        n2 = mul2048(n1)
        n2 = mix(n2, n1)
        n2 = prune(n2)

        curr_number = n2

    return curr_number


def run(file_name: str, num_rounds: int):
    numbers = read_input(file_name)
    end_numbers = []
    for n in numbers:
        end_numbers.append(calculate(n, num_rounds))
    print(end_numbers)
    print(sum(end_numbers))


def read_input(file_name):
    numbers = []
    with open(file_name, "r") as f:
        for line in f:
            numbers.append(int(line.strip()))
    return numbers


if __name__ == '__main__':
    # run("test-a.txt", 2000)
    run("input-a.txt", 2000)
