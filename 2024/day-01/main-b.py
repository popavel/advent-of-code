if __name__ == '__main__':
    list_0 = []
    list_1 = []
    with open('input-a.txt', 'r') as f:
        for line in f:
            line = line.split()
            line = list(map(int, line))
            list_0.append(line[0])
            list_1.append(line[1])

    score = 0
    for i in range(len(list_0)):
        score += list_0[i] * list_1.count(list_0[i])
    print(score)