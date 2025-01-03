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

    valid_middles = []
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
        if isValid:
            valid_middles.append(int(sequency[len(sequency)//2]))

    print(valid_middles)
    print(sum(valid_middles))