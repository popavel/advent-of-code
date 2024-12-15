def print_grid(grid):
    grid_as_string = ''
    for row in grid:
        row_as_string = ''.join(row)
        grid_as_string += row_as_string + '\n'
    print(grid_as_string)


def can_move(box: tuple[tuple, tuple, str]) -> bool:
    if box[2] == 'u':
        if grid[box[0][0] - 1][box[0][1]] == '.' and grid[box[1][0] - 1][box[1][1]] == '.':
            return True
        elif grid[box[0][0] - 1][box[0][1]] == '#' or grid[box[1][0] - 1][box[1][1]] == '#':
            return False
        elif grid[box[0][0] - 1][box[0][1]] == '[' and grid[box[1][0] - 1][box[1][1]] == ']':
            return can_move(((box[0][0] - 1, box[0][1]), (box[1][0] - 1, box[1][1]), 'u'))
        elif grid[box[0][0] - 1][box[0][1]] == ']' and grid[box[1][0] - 1][box[1][1]] == '[':
            return (
                    can_move(((box[0][0] - 1, box[0][1]-1), (box[1][0] - 1, box[0][1]), 'u'))
                    and can_move(((box[0][0] - 1, box[1][1]), (box[1][0] - 1, box[1][1]+1), 'u'))
                    )
        elif grid[box[0][0] - 1][box[0][1]] == ']':
            return can_move(((box[0][0] - 1, box[0][1]-1), (box[1][0] - 1, box[0][1]), 'u'))
        elif grid[box[1][0] - 1][box[1][1]] == '[':
            return can_move(((box[0][0] - 1, box[1][1]), (box[1][0] - 1, box[1][1]+1), 'u'))
        else:
            raise Exception
    elif box[2] == 'd':
        if grid[box[0][0] + 1][box[0][1]] == '.' and grid[box[1][0] + 1][box[1][1]] == '.':
            return True
        elif grid[box[0][0] + 1][box[0][1]] == '#' or grid[box[1][0] + 1][box[1][1]] == '#':
            return False
        elif grid[box[0][0] + 1][box[0][1]] == '[' and grid[box[1][0] + 1][box[1][1]] == ']':
            return can_move(((box[0][0] + 1, box[0][1]), (box[1][0] + 1, box[1][1]), 'd'))
        elif grid[box[0][0] + 1][box[0][1]] == ']' and grid[box[1][0] + 1][box[1][1]] == '[':
            return (
                    can_move(((box[0][0] + 1, box[0][1]-1), (box[1][0] + 1, box[0][1]), 'd'))
                    and can_move(((box[0][0] + 1, box[1][1]), (box[1][0] + 1, box[1][1]+1), 'd'))
            )
        elif grid[box[0][0] + 1][box[0][1]] == ']':
            return can_move(((box[0][0] + 1, box[0][1]-1), (box[1][0] + 1, box[0][1]), 'd'))
        elif grid[box[1][0] + 1][box[1][1]] == '[':
            return can_move(((box[0][0] + 1, box[1][1]), (box[1][0] + 1, box[1][1]+1), 'd'))
        else:
            raise Exception


def move(box: tuple[tuple, tuple, str]) -> None:
    if box[2] == 'u':
        if grid[box[0][0] - 1][box[0][1]] == '.' and grid[box[1][0] - 1][box[1][1]] == '.':
            pass
        elif grid[box[0][0] - 1][box[0][1]] == '[' and grid[box[1][0] - 1][box[1][1]] == ']':
            move(((box[0][0] - 1, box[0][1]), (box[1][0] - 1, box[1][1]), 'u'))
        elif grid[box[0][0] - 1][box[0][1]] == ']' and grid[box[1][0] - 1][box[1][1]] == '[':
            move(((box[0][0] - 1, box[0][1]-1), (box[1][0] - 1, box[0][1]), 'u'))
            move(((box[0][0] - 1, box[1][1]), (box[1][0] - 1, box[1][1]+1), 'u'))
        elif grid[box[0][0] - 1][box[0][1]] == ']':
            move(((box[0][0] - 1, box[0][1]-1), (box[1][0] - 1, box[0][1]), 'u'))
        elif grid[box[1][0] - 1][box[1][1]] == '[':
            move(((box[0][0] - 1, box[1][1]), (box[1][0] - 1, box[1][1]+1), 'u'))
        else:
            raise Exception
        grid[box[0][0] - 1][box[0][1]] = '['
        grid[box[1][0] - 1][box[1][1]] = ']'
        grid[box[0][0]][box[0][1]] = '.'
        grid[box[1][0]][box[1][1]] = '.'
    elif box[2] == 'd':
        if grid[box[0][0] + 1][box[0][1]] == '.' and grid[box[1][0] + 1][box[1][1]] == '.':
            pass
        elif grid[box[0][0] + 1][box[0][1]] == '[' and grid[box[1][0] + 1][box[1][1]] == ']':
            move(((box[0][0] + 1, box[0][1]), (box[1][0] + 1, box[1][1]), 'd'))
        elif grid[box[0][0] + 1][box[0][1]] == ']' and grid[box[1][0] + 1][box[1][1]] == '[':
            move(((box[0][0] + 1, box[0][1]-1), (box[1][0] + 1, box[0][1]), 'd'))
            move(((box[0][0] + 1, box[1][1]), (box[1][0] + 1, box[1][1]+1), 'd'))
        elif grid[box[0][0] + 1][box[0][1]] == ']':
            move(((box[0][0] + 1, box[0][1]-1), (box[1][0] + 1, box[0][1]), 'd'))
        elif grid[box[1][0] + 1][box[1][1]] == '[':
            move(((box[0][0] + 1, box[1][1]), (box[1][0] + 1, box[1][1]+1), 'd'))
        else:
            raise Exception
        grid[box[0][0] + 1][box[0][1]] = '['
        grid[box[1][0] + 1][box[1][1]] = ']'
        grid[box[0][0]][box[0][1]] = '.'
        grid[box[1][0]][box[1][1]] = '.'


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
                row = []
                for c in line.strip():
                    if c == '#':
                        row.append('#')
                        row.append('#')
                    elif c == 'O':
                        row.append('[')
                        row.append(']')
                    elif c == '.':
                        row.append('.')
                        row.append('.')
                    elif c == '@':
                        row.append('@')
                        row.append('.')
                grid.append(row)
            else:
                movements += line.strip()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                r = [i, j]

    print('initial state')
    print_grid(grid)

    for step, m in enumerate(movements):
        # print('step ', step)
        if m == '>':
            if grid[r[0]][r[1] + 1] == '.':
                grid[r[0]][r[1]] = '.'
                r[1] += 1
                grid[r[0]][r[1]] = '@'
            elif grid[r[0]][r[1] + 1] == '#':
                pass
            elif grid[r[0]][r[1] + 1] == '[':
                idx = r[1] + 3
                idx_dot = -1
                while idx_dot == -1 and grid[r[0]][idx] != '#':
                    if grid[r[0]][idx] == '.':
                        idx_dot = idx
                        break
                    idx += 2
                if idx_dot == -1:
                    pass
                else:
                    for i in reversed(range(r[1] + 2, idx_dot + 1)):
                        grid[r[0]][i] = grid[r[0]][i - 1]
                    grid[r[0]][r[1]] = '.'
                    r[1] += 1
                    grid[r[0]][r[1]] = '@'
        elif m == '<':
            if grid[r[0]][r[1] - 1] == '.':
                grid[r[0]][r[1]] = '.'
                r[1] -= 1
                grid[r[0]][r[1]] = '@'
            elif grid[r[0]][r[1] - 1] == '#':
                pass
            elif grid[r[0]][r[1] - 1] == ']':
                idx = r[1] - 3
                idx_dot = -1
                while idx_dot == -1 and grid[r[0]][idx] != '#':
                    if grid[r[0]][idx] == '.':
                        idx_dot = idx
                        break
                    idx -= 2
                if idx_dot == -1:
                    pass
                else:
                    for i in range(idx_dot, r[1] - 1):
                        grid[r[0]][i] = grid[r[0]][i + 1]
                    grid[r[0]][r[1]] = '.'
                    r[1] -= 1
                    grid[r[0]][r[1]] = '@'
        elif m == '^':
            if grid[r[0] - 1][r[1]] == '.':
                grid[r[0]][r[1]] = '.'
                r[0] -= 1
                grid[r[0]][r[1]] = '@'
            elif grid[r[0] - 1][r[1]] == '#':
                pass
            elif grid[r[0] - 1][r[1]] == '[':
                if can_move(((r[0] - 1, r[1]), (r[0] - 1, r[1] + 1), 'u')):
                    move(((r[0] - 1, r[1]), (r[0] - 1, r[1] + 1), 'u'))
                    grid[r[0]][r[1]] = '.'
                    r[0] -= 1
                    grid[r[0]][r[1]] = '@'
                else:
                    pass
            elif grid[r[0] - 1][r[1]] == ']':
                if can_move(((r[0] - 1, r[1] - 1), (r[0] - 1, r[1]), 'u')):
                    move(((r[0] - 1, r[1] - 1), (r[0] - 1, r[1]), 'u'))
                    grid[r[0]][r[1]] = '.'
                    r[0] -= 1
                    grid[r[0]][r[1]] = '@'
                else:
                    pass
        elif m == 'v':
            if grid[r[0] + 1][r[1]] == '.':
                grid[r[0]][r[1]] = '.'
                r[0] += 1
                grid[r[0]][r[1]] = '@'
            elif grid[r[0] + 1][r[1]] == '#':
                pass
            elif grid[r[0] + 1][r[1]] == '[':
                if can_move(((r[0] + 1, r[1]), (r[0] + 1, r[1] + 1), 'd')):
                    move(((r[0] + 1, r[1]), (r[0] + 1, r[1] + 1), 'd'))
                    grid[r[0]][r[1]] = '.'
                    r[0] += 1
                    grid[r[0]][r[1]] = '@'
                else:
                    pass
            elif grid[r[0] + 1][r[1]] == ']':
                if can_move(((r[0] + 1, r[1] - 1), (r[0] + 1, r[1]), 'd')):
                    move(((r[0] + 1, r[1] - 1), (r[0] + 1, r[1]), 'd'))
                    grid[r[0]][r[1]] = '.'
                    r[0] += 1
                    grid[r[0]][r[1]] = '@'
                else:
                    pass
        # print('move ', m)
        # print_grid(grid)

    print('final state')
    print_grid(grid)

    gps_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '[':
                gps_score += 100*i + j
    print(gps_score)
