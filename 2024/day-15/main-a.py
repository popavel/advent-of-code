def print_grid(grid):
    grid_as_string = ''
    for row in grid:
        row_as_string = ''.join(row)
        grid_as_string += row_as_string + '\n'
    print(grid_as_string)



if __name__ == '__main__':
    grid = []
    movements = ''
    with open('input-a.txt', 'r') as f:
        is_movement_line = False
        for line in f:
            if not line.strip():
                is_movement_line = True
                continue
            if not is_movement_line:
                grid.append(list(line.strip()))
            else:
                movements += line.strip()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                r = [i, j]

    print('initial state')
    print_grid(grid)

    for m in movements:
        if m == '>':
            if grid[r[0]][r[1] + 1] == '.':
                grid[r[0]][r[1]] = '.'
                r[1] += 1
                grid[r[0]][r[1]] = '@'
            elif grid[r[0]][r[1] + 1] == '#':
                pass
            elif grid[r[0]][r[1] + 1] == 'O':
                idx = r[1] + 2
                idx_dot = -1
                while idx_dot == -1 and grid[r[0]][idx] != '#':
                    if grid[r[0]][idx] == '.':
                        idx_dot = idx
                        break
                    idx += 1
                if idx_dot == -1:
                    pass
                else:
                    grid[r[0]][r[1]] = '.'
                    r[1] += 1
                    grid[r[0]][r[1]] = '@'
                    grid[r[0]][r[1]+1:idx_dot+1] = ['O']*(idx_dot-r[1])
        elif m == '<':
            if grid[r[0]][r[1] - 1] == '.':
                grid[r[0]][r[1]] = '.'
                r[1] -= 1
                grid[r[0]][r[1]] = '@'
            elif grid[r[0]][r[1] - 1] == '#':
                pass
            elif grid[r[0]][r[1] - 1] == 'O':
                idx = r[1] - 2
                idx_dot = -1
                while idx_dot == -1 and grid[r[0]][idx] != '#':
                    if grid[r[0]][idx] == '.':
                        idx_dot = idx
                        break
                    idx -= 1
                if idx_dot == -1:
                    pass
                else:
                    grid[r[0]][r[1]] = '.'
                    r[1] -= 1
                    grid[r[0]][r[1]] = '@'
                    grid[r[0]][idx_dot:r[1]] = ['O']*(r[1]-idx_dot)
        elif m == '^':
            if grid[r[0] - 1][r[1]] == '.':
                grid[r[0]][r[1]] = '.'
                r[0] -= 1
                grid[r[0]][r[1]] = '@'
            elif grid[r[0] - 1][r[1]] == '#':
                pass
            elif grid[r[0] - 1][r[1]] == 'O':
                idx = r[0] - 2
                idx_dot = -1
                while idx_dot == -1 and grid[idx][r[1]] != '#':
                    if grid[idx][r[1]] == '.':
                        idx_dot = idx
                        break
                    idx -= 1
                if idx_dot == -1:
                    pass
                else:
                    grid[r[0]][r[1]] = '.'
                    r[0] -= 1
                    grid[r[0]][r[1]] = '@'
                    for i in range(idx_dot, r[0]):
                        grid[i][r[1]] = 'O'
        elif m == 'v':
            if grid[r[0] + 1][r[1]] == '.':
                grid[r[0]][r[1]] = '.'
                r[0] += 1
                grid[r[0]][r[1]] = '@'
            elif grid[r[0] + 1][r[1]] == '#':
                pass
            elif grid[r[0] + 1][r[1]] == 'O':
                idx = r[0] + 2
                idx_dot = -1
                while idx_dot == -1 and grid[idx][r[1]] != '#':
                    if grid[idx][r[1]] == '.':
                        idx_dot = idx
                        break
                    idx += 1
                if idx_dot == -1:
                    pass
                else:
                    grid[r[0]][r[1]] = '.'
                    r[0] += 1
                    grid[r[0]][r[1]] = '@'
                    for i in range(r[0]+1, idx_dot+1):
                        grid[i][r[1]] = 'O'
        # print('move ', m)
        # print_grid(grid)
    print('final state')
    print_grid(grid)

    gps_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'O':
                gps_score += 100*i + j
    print(gps_score)