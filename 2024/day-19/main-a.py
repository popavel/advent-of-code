if __name__ == '__main__':
    b = []
    with open('test-a.txt', 'r') as f:
        for line in f:
            line = list(map(int, line.strip().split(',')))
            b.append((line[0], line[1]))