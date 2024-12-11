TEST_0 = [0, 1, 10, 99, 999]
TEST_1 = [125, 17]
INPUT = [3279, 998884, 1832781, 517, 8, 18864, 28, 0]
STEPS = 25
if __name__ == '__main__':
    stones = INPUT
    for _ in range(STEPS):
        new_stones = []
        for i in stones:
            if i == 0:
                new_stones.append(1)
            elif len(str(i)) % 2 == 0:
                left = int(str(i)[:len(str(i))//2])
                right = int(str(i)[len(str(i))//2:])
                new_stones.append(left)
                new_stones.append(right)
            else:
                new_stones.append(i*2024)
        stones = new_stones

    print(stones)
    print(len(stones))