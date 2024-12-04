import re

if __name__ == '__main__':
    grid = []
    grid_reversed = []
    with open('input-a.txt', 'r') as f:
        for line in f:
            grid += [line.strip()]
            grid_reversed += [line.strip()[::-1]]

    grid_transposed = list(map(lambda t: ''.join(t), zip(*grid)))
    grid_transposed_reversed = []
    for line in grid_transposed:
        grid_transposed_reversed += [line[::-1]]

    count_horizonntal = 0
    for line in grid:
        count_horizonntal += len(re.findall(r'XMAS', line))
        count_horizonntal += len(re.findall(r'SAMX', line))

    count_vertical = 0
    for line in grid_transposed:
        count_vertical += len(re.findall(r'XMAS', line))
        count_vertical += len(re.findall(r'SAMX', line))

    count_diagonal = 0
    for i in range(len(grid[0]) - 3):
        for j in range(len(grid) - 3):
            count_diagonal += len(re.findall(r'XMAS', grid[j][i] + grid[j+1][i+1] + grid[j+2][i+2] + grid[j+3][i+3]))
            count_diagonal += len(re.findall(r'SAMX', grid[j][i] + grid[j+1][i+1] + grid[j+2][i+2] + grid[j+3][i+3]))
            count_diagonal += len(re.findall(r'XMAS', grid_reversed[j][i] + grid_reversed[j+1][i+1] + grid_reversed[j+2][i+2] + grid_reversed[j+3][i+3]))
            count_diagonal += len(re.findall(r'SAMX', grid_reversed[j][i] + grid_reversed[j+1][i+1] + grid_reversed[j+2][i+2] + grid_reversed[j+3][i+3]))

    print(count_horizonntal + count_vertical + count_diagonal)


