from functools import reduce


def run(file_name: str) -> None:
    with open(file_name) as f:
        paper = 0
        ribbon = 0
        for line in f:
            nums = sorted([int(n) for n in line.strip().split('x')])
            a = nums[0] * nums[1]
            b = nums[0] * nums[2]
            c = nums[1] * nums[2]
            paper += 2 * a + 2 * b + 2 * c + a
            ribbon += reduce(lambda x, y: x * y, nums) + 2 * nums[0] + 2 * nums[1]
    print(f"paper: {paper}\nribbon: {ribbon}")


if __name__ == '__main__':
    run("input.txt")
