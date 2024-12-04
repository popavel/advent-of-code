if __name__ == '__main__':
    grid = []
    with open('input-a.txt', 'r') as f:
        for line in f:
            grid += [line.strip()]

    count = 0
    for j in range(1, len(grid[0])-1):
        for i in range(1, len(grid)-1):
            if grid[i][j] == 'A':
                if (
                        (grid[i-1][j-1] == "M" and grid[i-1][j+1] == "S" and grid[i+1][j-1] == "M" and grid[i+1][j+1] == "S")
                        or (grid[i-1][j-1] == "S" and grid[i-1][j+1] == "S" and grid[i+1][j-1] == "M" and grid[i+1][j+1] == "M")
                        or (grid[i-1][j-1] == "S" and grid[i-1][j+1] == "M" and grid[i+1][j-1] == "S" and grid[i+1][j+1] == "M")
                        or (grid[i-1][j-1] == "M" and grid[i-1][j+1] == "M" and grid[i+1][j-1] == "S" and grid[i+1][j+1] == "S")
                ):
                    count += 1

    print(count)

