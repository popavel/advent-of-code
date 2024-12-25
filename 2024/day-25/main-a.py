import numpy as np


def convert2vector(curr_input: list[str]) -> np.array:
    v = np.zeros(len(curr_input[0]), dtype=np.int32)
    for row in curr_input:
        for i in range(len(row)):
            if row[i] == '#':
                v[i] += 1
    return v


def read_input(file_name: str) -> tuple[np.array, np.array]:
    locks = []
    keys = []
    with open(file_name, "r") as file:
        curr_input = []
        for line in file:
            line = line.strip()
            if len(line) == 0:
                if curr_input[0][0] == '#':
                    locks.append(convert2vector(curr_input))
                else:
                    keys.append(convert2vector(curr_input))
                curr_input = []
            else:
                curr_input.append(line)

    if curr_input[0][0] == '#':
        locks.append(convert2vector(curr_input))
    else:
        keys.append(convert2vector(curr_input))

    return locks, keys


def run(file_name: str):
    locks, keys = read_input(file_name)

    count = 0
    for lock in locks:
        for key in keys:
            if np.all((lock + key) <= 7):
                count += 1

    print(count)


if __name__ == '__main__':
    # run("test-a.txt")
    run("input-a.txt")
