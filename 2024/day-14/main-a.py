from functools import reduce
from math import prod

m_test = 7
n_test = 11
m_input = 103
n_input = 101
iter_test = 100
if __name__ == '__main__':
    pvs = []
    m = m_input
    n = n_input
    iter = iter_test
    with open('input-a.txt', 'r') as f:
        for line in f:
            p_v = line.strip().split()
            if len(p_v) != 2:
                raise ValueError(f'invalid line: {line}')
            p = list(map(int, p_v[0][2:].split(',')))
            v = list(map(int, p_v[1][2:].split(',')))
            pvs.append((p, v))

    pvs_moved = [(lambda p, v: ((p[0]+v[0]*iter)%n, (p[1]+v[1]*iter)%m))(p,v) for p, v in pvs]

    counts = [0,0,0,0]
    m_middle = m//2
    n_middle = n//2
    for p in pvs_moved:
        if p[0] < n_middle and p[1] < m_middle:
            counts[0] += 1
        elif p[0] < n_middle and p[1] > m_middle:
            counts[1] += 1
        elif p[0] > n_middle and p[1] < m_middle:
            counts[2] += 1
        elif p[0] > n_middle and p[1] > m_middle:
            counts[3] += 1

    print(counts)
    print(prod(counts))