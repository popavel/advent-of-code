def evaluate(op, regs):
    match op:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return regs['A']
        case 5:
            return regs['B']
        case 6:
            return regs['C']
        case 7:
            raise ValueError(f'Reserved value {op}')
        case _:
            raise ValueError(f'Unknown value {op}')


def evaluate_program(a_new, p):
    regs = {'A': a_new, 'B': 0, 'C': 0}
    output = []
    idx = 0
    while idx < len(p):
        instr = p[idx]
        op = p[idx + 1]
        match instr:
            case 0:
                a = regs['A']
                res = a // (2 ** evaluate(op, regs))
                regs['A'] = res
            case 1:
                b = regs['B']
                res = b ^ op
                regs['B'] = res
            case 2:
                res = evaluate(op, regs) % 8
                regs['B'] = res
            case 3:
                a = regs['A']
                if a != 0:
                    idx = op
                    continue
            case 4:
                b = regs['B']
                c = regs['C']
                res = b ^ c
                regs['B'] = res
            case 5:
                res = evaluate(op, regs) % 8
                output.append(res)
            case 6:
                a = regs['A']
                res = a // (2 ** evaluate(op, regs))
                regs['B'] = res
            case 7:
                a = regs['A']
                res = a // (2 ** evaluate(op, regs))
                regs['C'] = res
            case _:
                raise ValueError(f'Unknown instruction {instr}')
        idx += 2
    return output


if __name__ == '__main__':
    start_test = {'A': 729, 'B': 0, 'C': 0}
    p_test = [0, 1, 5, 4, 3, 0]
    start_input = {'A': 64584136, 'B': 0, 'C': 0}
    p_input = [2, 4, 1, 2, 7, 5, 1, 3, 4, 3, 5, 5, 0, 3, 3, 0]

    start_b = {'A': 2024, 'B': 0, 'C': 0}
    start_b1 = {'A': 117440, 'B': 0, 'C': 0}
    input_b = [0, 3, 5, 4, 3, 0]

    p = p_input
    regs = start_input

    a = 1
    idx = len(p) - 2
    for output in reversed(p[:-1]):
        print(a)
        a_new = a * 8
        stop = False
        i = 0
        while not stop:
            output_values = evaluate_program(a_new + i, p)
            print(output_values)
            if output_values == p[idx:]:
                a_new += i
                stop = True
                break
            if not stop:
                i += 1
        a = a_new
        idx -= 1

    print(a)
