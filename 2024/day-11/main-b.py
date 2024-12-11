TEST_0 = [0, 1, 10, 99, 999]
TEST_1 = [125, 17]
INPUT = [3279, 998884, 1832781, 517, 8, 18864, 28, 0]
STEPS = 75
if __name__ == '__main__':
    stones = INPUT
    counts = {}
    for i in stones:
        if i in counts.keys():
            counts[i] += 1
        else:
            counts[i] = 1

    print(counts)
    for _ in range(STEPS):
        new_counts = {}
        for k in counts.keys():
            if k == 0:
                if 1 in new_counts.keys():
                    new_counts[1] += counts[0]
                else:
                    new_counts[1] = counts[0]
            elif len(str(k)) % 2 == 0:
                left = int(str(k)[:len(str(k)) // 2])
                right = int(str(k)[len(str(k)) // 2:])
                if left in new_counts.keys():
                    new_counts[left] += counts[k]
                else:
                    new_counts[left] = counts[k]
                if right in new_counts.keys():
                    new_counts[right] += counts[k]
                else:
                    new_counts[right] = counts[k]
            else:
                if k * 2024 in new_counts.keys():
                    new_counts[k * 2024] += counts[k]
                else:
                    new_counts[k * 2024] = counts[k]
        counts = new_counts

    print(counts)
    print(len(counts))
    print(sum(counts.values()))
