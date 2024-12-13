import numpy as np


if __name__ == '__main__':
    with open('input-a.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    input_data = []
    for i in range(0, len(lines), 3):
        a = lines[i][lines[i].index(':')+1:].split(',')
        a = [el.strip() for el in a]
        a[0] = a[0][2:]
        a[1] = a[1][2:]
        a = list(map(int, a))

        b = lines[i+1][lines[i+1].index(':')+1:].split(',')
        b = [el.strip() for el in b]
        b[0] = b[0][2:]
        b[1] = b[1][2:]
        b = list(map(int, b))

        result = lines[i+2][lines[i+2].index(':')+1:].split(',')
        result = [el.strip() for el in result]
        result[0] = result[0][2:]
        result[1] = result[1][2:]
        result = list(map(int, result))
        result = [i + 10_000_000_000_000 for i in result]

        input_data.append((a, b, result))

    tokens = []
    for a, b, result in input_data:
        A = np.array([[a[0], b[0]], [a[1], b[1]]])
        B = np.array([result[0], result[1]])
        x = np.linalg.solve(A, B)
        print(x)
        x_int = np.rint(x)
        if abs(x[0] - x_int[0]) < 0.0001 and abs(x[1] - x_int[1]) < 0.0001:
            if x[0] < 0 or x[1] < 0:
                raise Exception('Negative values')
            tokens.append(x[0]*3 + x[1])

    print(sum(tokens))