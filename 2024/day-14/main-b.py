from functools import reduce
from math import prod, sqrt

m_test = 7
n_test = 11
m_input = 103
n_input = 101
iter_test = 100
if __name__ == '__main__':
    pvs = []
    m = m_input
    n = n_input
    with open('input-a.txt', 'r') as f:
        for line in f:
            p_v = line.strip().split()
            if len(p_v) != 2:
                raise ValueError(f'invalid line: {line}')
            p = list(map(int, p_v[0][2:].split(',')))
            v = list(map(int, p_v[1][2:].split(',')))
            pvs.append((p, v))

    m_middle = m//2
    n_middle = n//2
    dist = 0
    for p, v in pvs:
        dist += sqrt((p[0] - n_middle)**2 + (p[1] - m_middle)**2)
    iter = 0
    distances = [dist]
    while iter<10001:
        iter += 1
        pvs_moved = [(lambda p, v: ((p[0]+v[0]*iter)%n, (p[1]+v[1]*iter)%m))(p,v) for p, v in pvs]
        new_dist = 0
        for p in pvs_moved:
            new_dist += sqrt((p[0] - n_middle)**2 + (p[1] - m_middle)**2)
        distances.append(new_dist)

    min_d = min(distances)
    print(distances.index(min_d), min_d)
