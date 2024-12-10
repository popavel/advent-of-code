if __name__ == '__main__':
    grid = []
    with open('input-a.txt', 'r') as f:
        for line in f:
            input_line = line.strip()
            grid.append([int(c) for c in input_line])
