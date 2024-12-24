from graph import Node


def read_input(file_name: str) -> tuple[dict[str, int], dict[str, tuple[str, str, str]]]:
    with open(file_name, 'r') as file:
        wire_value = {}
        line = file.readline().strip()
        while line:
            wire, value = line.split()
            wire = wire.strip()[:-1]
            value = int(value.strip())
            wire_value[wire] = value

            line = file.readline().strip()

        wire_parent_and_operation = {}
        line = file.readline().strip()
        while line:
            par_and_op, wire = line.split('->')
            wire = wire.strip()
            par0, op, par1 = par_and_op.split()
            par0 = par0.strip()
            op = op.strip()
            par1 = par1.strip()
            if par0 == par1:
                raise ValueError(f"Invalid operation: {par0} {op} {par1}")
            if par1 < par0:
                par0, par1 = par1, par0
            wire_parent_and_operation[wire] = (par0, par1, op)

            line = file.readline().strip()

    return wire_value, wire_parent_and_operation


def zs2decimal(zs: list[int]) -> int:
    int_as_str = ''.join([str(z) for z in zs])
    return int(int_as_str, 2)


def compute_value(v0: int, v1: int, op: str) -> int:
    match op:
        case 'AND':
            return v0 & v1
        case 'OR':
            return v0 | v1
        case 'XOR':
            return v0 ^ v1
        case _:
            raise ValueError(f"Invalid operation: {op}")


def run(file_name: str):
    wire_value, wire_parent_and_operation = read_input(file_name)
    wire_parent_and_operation_reversed = {v: k for k, v in wire_parent_and_operation.items()}

    wrong_pairs_manually = ['z37', 'vkg', 'z20', 'cqr', 'nfj', 'ncd', 'z15', 'qnw']
    print(','.join(sorted(wrong_pairs_manually)))


def get_graph(wire_value: dict[str, int], wire_parent_and_operation: dict[str, tuple[str, str, str]]) -> list[Node]:
    nodes = {}

    for w in wire_value.keys():
        nodes[w] = Node(w)

    for w, p_and_op in wire_parent_and_operation.items():
        node = Node(w)
        node.degree = 2
        nodes[w] = node

    for w, p_and_op in wire_parent_and_operation.items():
        par0, par1, _ = p_and_op
        nodes[par0].neighbors.append(nodes[w])
        nodes[par1].neighbors.append(nodes[w])

    return sorted(nodes.values(), key=lambda n: n.degree)


if __name__ == '__main__':
    # run("test-a.txt")
    # run("test-a1.txt")
    run("input-incorrect-wires-swapped-back.txt")
