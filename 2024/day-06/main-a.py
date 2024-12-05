if __name__ == '__main__':
    grid = []
    grid_reversed = []
    with open('input-a.txt', 'r') as f:
        for line in f:
            grid += [line.strip()]
            grid_reversed += [line.strip()[::-1]]