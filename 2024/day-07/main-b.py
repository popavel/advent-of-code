def check_equation(y: int, xs: list[int]) -> bool:
    if len(xs) == 0:
        return False

    previous = [xs[0]]
    for i in range(1, len(xs), 1):
        next = [0] * (len(previous) * 3)
        for j in range(0, len(previous), 1):
            next[j] = previous[j] + xs[i]
            next[j+len(previous)] = previous[j] * xs[i]
            next[j+len(previous)*2] = int(str(previous[j]) + str(xs[i]))
        previous = next

    return True if y in previous else False


if __name__ == '__main__':
    ys = []
    xs = []
    with open('input-a.txt', 'r') as f:
        for line in f:
            y_and_x = line.strip().split(':')
            ys += [int(y_and_x[0])]
            xs += [[int(i) for i in y_and_x[1].split()]]

    result = 0
    for i in range(len(ys)):
        if check_equation(ys[i], xs[i]):
            print(ys[i])
            result += ys[i]

    print(result)
