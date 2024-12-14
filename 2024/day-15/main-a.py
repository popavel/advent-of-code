if __name__ == '__main__':
    grid = []
    with open('test-a.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())