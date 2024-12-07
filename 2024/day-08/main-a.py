if __name__ == '__main__':
    ys = []
    xs = []
    with open('input-a.txt', 'r') as f:
        for line in f:
            y_and_x = line.strip().split(':')
            ys += [int(y_and_x[0])]
            xs += [[int(i) for i in y_and_x[1].split()]]
