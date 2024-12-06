if __name__ == '__main__':
    grid_string = []
    with open('input-a.txt', 'r') as f:
        for line in f:
            grid_string += [line.strip()]

    grid = [[0]*len(grid_string[0]) for i in range(len(grid_string))]

    guard_i = -1
    guard_j = -1
    for i in range(len(grid_string)):
        for j in range(len(grid_string[0])):
            if grid_string[i][j] == '#':
                grid[i][j] = -1
            elif grid_string[i][j] == '^':
                guard_i = i
                guard_j = j

    guard_dir = 'u'
    isInGrid = True
    while isInGrid:
        grid[guard_i][guard_j] = 1
        if guard_dir == 'u':
            if guard_i == 0:
                isInGrid = False
            elif grid[guard_i-1][guard_j] == -1:
                guard_dir = 'r'
            else:
                guard_i -= 1
        elif guard_dir == 'd':
            if guard_i == len(grid)-1:
                isInGrid = False
            elif grid[guard_i+1][guard_j] == -1:
                guard_dir = 'l'
            else:
                guard_i += 1
        elif guard_dir == 'l':
            if guard_j == 0:
                isInGrid = False
            elif grid[guard_i][guard_j-1] == -1:
                guard_dir = 'u'
            else:
                guard_j -= 1
        elif guard_dir == 'r':
            if guard_j == len(grid[0])-1:
                isInGrid = False
            elif grid[guard_i][guard_j+1] == -1:
                guard_dir = 'd'
            else:
                guard_j += 1

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                count += 1

    print(count)

