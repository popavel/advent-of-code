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

        input_data.append((a, b, result))

    tokens = []
    for a, b, result in input_data:
        combinations = [ [(0,0)]*101 for i in range(101) ]
        for i in range(101):
            for j in range(101):
                combinations[i][j] = (a[0]*i + b[0]*j, a[1]*i + b[1]*j)

        prices = []
        for i in range(101):
            for j in range(101):
                if combinations[i][j] == (result[0], result[1]):
                    prices.append(i*3 + j)
        if len(prices) > 0:
            tokens.append(min(prices))

    print(tokens)
    print(sum(tokens))