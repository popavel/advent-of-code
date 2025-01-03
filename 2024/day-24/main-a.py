from graph import Node, topological_sort


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
    nodes = get_graph(wire_value, wire_parent_and_operation)
    nodes = topological_sort(nodes)
    for n in nodes:
        if n.value in wire_value.keys():
            continue
        par0, par1, op = wire_parent_and_operation[n.value]
        v0 = wire_value[par0]
        v1 = wire_value[par1]
        res = compute_value(v0, v1, op)
        wire_value[n.value] = res

    zs = {}
    for w, v in wire_value.items():
        if w[0] == 'z':
            zs[w] = v
    zs = sorted(zs.items(), key=lambda x: x[0])
    zs = list(reversed([x[1] for x in zs]))

    result = zs2decimal(zs)
    print(result)


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
    run("input-a.txt")
