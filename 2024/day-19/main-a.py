def is_possible(design: str, patterns: list[str]) -> bool:
    subdesigns_possible = [0] * (len(design)+1)
    subdesigns_possible[0] = 1

    for i in range(1, len(subdesigns_possible)):
        for j in range(i):
            if subdesigns_possible[i-j-1] > 0 and design[i-j-1:i] in patterns:
                subdesigns_possible[i] = 1
                break

    return subdesigns_possible[-1] > 0


if __name__ == '__main__':
    with open('input-a.txt', 'r') as f:
        patterns = list(map(lambda s: s.strip(), f.readline().strip().split(',')))
        f.readline()
        designs = []
        while True:
            line = f.readline().strip()
            if not line:
                break
            designs.append(line)

    count = 0
    for design in designs:
        if is_possible(design, patterns):
            print(design)
            count += 1

    print(count)
