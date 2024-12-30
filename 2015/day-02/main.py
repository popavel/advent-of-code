def run(file_name: str) -> None:
    with open(file_name) as f:
        paper = 0
        ribbon = 0
        for line in f:
            a, b, c = sorted([int(n) for n in line.strip().split('x')])
            paper += 2 * a * b + 2 * b * c + 2 * c * a + a * b
            ribbon += a * b * c + 2 * a + 2 * b
    print(f"paper: {paper}\nribbon: {ribbon}")


if __name__ == '__main__':
    run("input.txt")
