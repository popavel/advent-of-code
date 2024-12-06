def check_position(grid, guard_i, guard_j, guard_dir):
    locations = []
    for i in range(len(grid)):
        locations += [[]]
        for j in range(len(grid[0])):
            locations[i] += [[]]

    isInGrid = True
    while isInGrid:
        locations[guard_i][guard_j] += [guard_dir]

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

        if guard_dir in locations[guard_i][guard_j]:
            break

    return 1 if isInGrid else 0


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

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            guard_dir = 'u'
            if grid[i][j] == 0 and not (i == guard_i and j == guard_j):
                grid[i][j] = -1
                inGrid = check_position(grid, guard_i, guard_j, guard_dir)
                if inGrid == 1:
                    print(i, j)
                    count += 1
                grid[i][j] = 0

    print(count)

