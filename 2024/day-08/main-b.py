from curses.ascii import isdigit, isalpha
from itertools import combinations

if __name__ == '__main__':
    antennas = {}
    with open('input-a.txt', 'r') as f:
        for i, line in enumerate(f):
            line = line.strip()
            for j, c in enumerate(line):
                if isdigit(c) or isalpha(c):
                    if antennas.get(c) is None:
                        antennas[c] = [(i,j)]
                    else:
                        antennas[c].append((i,j))
    m = i + 1
    n = len(line)

    pairs = []
    for _, v in antennas.items():
        if len(v) > 1:
            pairs += list(combinations(v, 2))

    antinodes = set()
    for p in pairs:
        x1, y1 = p[0]
        antinodes.add((x1, y1))
        x2, y2 = p[1]
        antinodes.add((x2, y2))
        x_diff = abs(x1 - x2)
        y_diff = abs(y1 - y2)
        if x1<=x2 and y1 <= y2:
            x1_new = x1 - x_diff
            y1_new = y1 - y_diff
            while 0 <= x1_new < m and 0 <= y1_new < n:
                antinodes.add((x1_new, y1_new))
                x1_new -= x_diff
                y1_new -= y_diff
            x2_new = x2 + x_diff
            y2_new = y2 + y_diff
            while 0 <= x2_new < m and 0 <= y2_new < n:
                antinodes.add((x2_new, y2_new))
                x2_new += x_diff
                y2_new += y_diff
        elif x1<=x2 and y1 > y2:
            x1_new = x1 - x_diff
            y1_new = y1 + y_diff
            while 0 <= x1_new < m and 0 <= y1_new < n:
                antinodes.add((x1_new, y1_new))
                x1_new -= x_diff
                y1_new += y_diff
            x2_new = x2 + x_diff
            y2_new = y2 - y_diff
            while 0 <= x2_new < m and 0 <= y2_new < n:
                antinodes.add((x2_new, y2_new))
                x2_new += x_diff
                y2_new -= y_diff
        elif x1>x2 and y1 <= y2:
            x1_new = x1 + x_diff
            y1_new = y1 - y_diff
            while 0 <= x1_new < m and 0 <= y1_new < n:
                antinodes.add((x1_new, y1_new))
                x1_new += x_diff
                y1_new -= y_diff
            x2_new = x2 - x_diff
            y2_new = y2 + y_diff
            while 0 <= x2_new < m and 0 <= y2_new < n:
                antinodes.add((x2_new, y2_new))
                x2_new -= x_diff
                y2_new += y_diff
        elif x1>x2 and y1 > y2:
            x1_new = x1 + x_diff
            y1_new = y1 + y_diff
            while 0 <= x1_new < m and 0 <= y1_new < n:
                antinodes.add((x1_new, y1_new))
                x1_new += x_diff
                y1_new += y_diff
            x2_new = x2 - x_diff
            y2_new = y2 - y_diff
            while 0 <= x2_new < m and 0 <= y2_new < n:
                antinodes.add((x2_new, y2_new))
                x2_new -= x_diff
                y2_new -= y_diff

    print(len(antinodes))