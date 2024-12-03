import re

if __name__ == '__main__':
    muls_list = []
    with open('input-a.txt', 'r') as f:
        for line in f:
            muls = re.findall(r'mul\([\d]{1,3},[\d]{1,3}\)', line)
            print(muls)
            muls_list += muls
    print(muls_list)

    muls_list = list(map(lambda x: x[4:-1].split(','), muls_list))
    print(muls_list)
    muls_list = list(map(lambda x: int(x[0]) * int(x[1]), muls_list))
    print(sum(muls_list))
    # 164730528