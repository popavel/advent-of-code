if __name__ == '__main__':
    reports = []
    with open('input-a.txt', 'r') as f:
        for line in f:
            line = line.split()
            line = list(map(int, line))
            reports += [line]

    total_safe = 0
    for report in reports:
        if report[0] == report[1]:
            continue

        is_safe = True
        is_increasing = report[0] < report[1]
        for i in range(len(report) - 1):
            diff = report[i + 1] - report[i]
            if abs(diff) > 3:
                is_safe = False
                break
            elif diff < 0 and is_increasing:
                is_safe = False
                break
            elif diff > 0 and not is_increasing:
                is_safe = False
                break
            elif diff == 0:
                is_safe = False
                break
        if is_safe:
            total_safe += 1

    print(total_safe)
