def read_input(file_name: str) -> list[str]:
    grid = []
    with open(file_name, 'r') as f:
        for line in f:
            grid.append(line.strip())
    return grid


def run(input_file: str):
    grid = read_input(input_file)


if __name__ == '__main__':
    run("test-a.txt")