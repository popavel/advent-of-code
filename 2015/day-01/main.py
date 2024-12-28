def run(file_name: str, task_number: int) -> None:
    with open(file_name) as f:
        string = f.read()

    floor = 0
    for i, c in enumerate(string):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        if task_number == 1:
            if floor == -1:
                print(i+1)
                break

    if task_number == 0:
        print(floor)


if __name__ == '__main__':
    run("input.txt", 1)
