if __name__ == '__main__':
    with open('input-a.txt', 'r') as f:
        for line in f:
            input_line = line.strip()

    id_file = 0
    blocks_list = []
    for idx, i in enumerate(input_line):
        if idx % 2 == 0:
            for k in range(int(i)):
                blocks_list.append(id_file)
            id_file += 1
        else:
            for k in range(int(i)):
                blocks_list.append(-1)

    i = 0
    while blocks_list[i] != -1:
        i += 1
    j = len(blocks_list) - 1
    while blocks_list[j] == -1:
        j -= 1
    while i < j:
        blocks_list[i], blocks_list[j] = blocks_list[j], blocks_list[i]
        while blocks_list[i] != -1:
            i += 1
        while blocks_list[j] == -1:
            j -= 1

    count = 0
    i = 0
    while blocks_list[i] != -1:
        count += i * blocks_list[i]
        i += 1

    print(count)