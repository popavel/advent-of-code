if __name__ == '__main__':
    orderings = {}
    with open('input-a0.txt', 'r') as f:
        for line in f:
            ordering = line.strip().split('|')
            if orderings.get(ordering[0]) is not None:
                orderings[ordering[0]] += [ordering[1]]
            else:
                orderings[ordering[0]] = [ordering[1]]
    print(orderings)

    sequencies = []
    with open('input-a1.txt', 'r') as f:
        for line in f:
            sequencies.append(line.strip().split(','))
    print(sequencies)

    invalid_sequences = []
    for sequency in sequencies:
        isValid = True
        for i, p in enumerate(sequency):
            p_orderings = orderings.get(p)
            if p_orderings is None:
                continue
            for page in p_orderings:
                try:
                    index = sequency.index(page)
                except:
                    pass
                else:
                    if index < i:
                        isValid = False
                        break
            if not isValid:
                break
        if not isValid:
            invalid_sequences.append(sequency)

    print(invalid_sequences)

    rectified_sequences = []
    for sequency in invalid_sequences:
        rectified_sequency = ['-1'] * len(sequency)
        for i, p in enumerate(sequency):
            index = -1
            p_orderings = orderings.get(p)
            if p_orderings is None:
                index = len(sequency) - 1
            else:
                common_numbers = set(sequency) & set(p_orderings)
                index = len(sequency) - len(common_numbers) - 1
            rectified_sequency[index] = p
        rectified_sequences.append(rectified_sequency)

    print(rectified_sequences)

    valid_middles = []
    for sequency in rectified_sequences:
        valid_middles.append(int(sequency[len(sequency)//2]))

    print(valid_middles)
    print(sum(valid_middles))