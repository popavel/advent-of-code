if __name__ == '__main__':
    with open('input-a.txt', 'r') as f:
        for line in f:
            input_line = line.strip()

    id_file = 0
    blocks_list = []
    for idx, i in enumerate(input_line):
        if idx % 2 == 0:
            for k in range(int(i)):
                blocks_list.append((id_file, int(i)))
            id_file += 1
        else:
            for k in reversed(range(1, int(i)+1)):
                blocks_list.append((-1, k))

    print(blocks_list)

    j = len(blocks_list) - 1
    while j > 0:
        while j >= 0 and blocks_list[j][0] == -1:
            j -= 1
        i = 0
        while (i < j
               and (blocks_list[i][0] != -1
                    or (blocks_list[i][0] == -1 and blocks_list[i][1] < blocks_list[j][1]))
               ):
            i += 1
        if i < j:
            for k in range(blocks_list[j][1]):
                blocks_list[i+k] = blocks_list[j-k]
                blocks_list[j-k] = (-1, k+1)
        j -= blocks_list[j][1]

    count = 0
    for i, (id_file, _) in enumerate(blocks_list):
        if id_file != -1:
            count += i * id_file

    print(count)