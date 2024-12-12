class Node:
    def __init__(self, x: int, y: int, value: str):
        self.x = x
        self.y = y
        self.value = value
        self.neighbours = []
        self.vertices = 0
        self.visited = False

    def __str__(self):
        return f'Node({self.x}, {self.y}, {self.value}, vertices: {self.vertices}, neighbours: {[(n.x, n.y) for n in self.neighbours]})'

    def __repr__(self):
        return self.__str__()


def create_graph(grid: list[str]) -> list[list[Node]]:
    nodes = []
    for x, row in enumerate(grid):
        nodes.append([])
        for y, value in enumerate(row):
            nodes[x].append(Node(x, y, value))

    for x, row in enumerate(nodes):
        for y, node in enumerate(row):
            if x == 0:
                if y == 0:
                    if nodes[x][y + 1].value == node.value:
                        node.neighbours.append(nodes[x][y + 1])
                    if nodes[x + 1][y].value == node.value:
                        node.neighbours.append(nodes[x + 1][y])
                elif y == len(row) - 1:
                    if nodes[x][y - 1].value == node.value:
                        node.neighbours.append(nodes[x][y - 1])
                    if nodes[x + 1][y].value == node.value:
                        node.neighbours.append(nodes[x + 1][y])
                else:
                    if nodes[x][y - 1].value == node.value:
                        node.neighbours.append(nodes[x][y - 1])
                    if nodes[x][y + 1].value == node.value:
                        node.neighbours.append(nodes[x][y + 1])
                    if nodes[x + 1][y].value == node.value:
                        node.neighbours.append(nodes[x + 1][y])
            elif x == len(nodes) - 1:
                if y == 0:
                    if nodes[x][y + 1].value == node.value:
                        node.neighbours.append(nodes[x][y + 1])
                    if nodes[x - 1][y].value == node.value:
                        node.neighbours.append(nodes[x - 1][y])
                elif y == len(row) - 1:
                    if nodes[x][y - 1].value == node.value:
                        node.neighbours.append(nodes[x][y - 1])
                    if nodes[x - 1][y].value == node.value:
                        node.neighbours.append(nodes[x - 1][y])
                else:
                    if nodes[x][y - 1].value == node.value:
                        node.neighbours.append(nodes[x][y - 1])
                    if nodes[x][y + 1].value == node.value:
                        node.neighbours.append(nodes[x][y + 1])
                    if nodes[x - 1][y].value == node.value:
                        node.neighbours.append(nodes[x - 1][y])
            else:
                if y == 0:
                    if nodes[x][y + 1].value == node.value:
                        node.neighbours.append(nodes[x][y + 1])
                    if nodes[x - 1][y].value == node.value:
                        node.neighbours.append(nodes[x - 1][y])
                    if nodes[x + 1][y].value == node.value:
                        node.neighbours.append(nodes[x + 1][y])
                elif y == len(row) - 1:
                    if nodes[x][y - 1].value == node.value:
                        node.neighbours.append(nodes[x][y - 1])
                    if nodes[x - 1][y].value == node.value:
                        node.neighbours.append(nodes[x - 1][y])
                    if nodes[x + 1][y].value == node.value:
                        node.neighbours.append(nodes[x + 1][y])
                else:
                    if nodes[x][y - 1].value == node.value:
                        node.neighbours.append(nodes[x][y - 1])
                    if nodes[x][y + 1].value == node.value:
                        node.neighbours.append(nodes[x][y + 1])
                    if nodes[x - 1][y].value == node.value:
                        node.neighbours.append(nodes[x - 1][y])
                    if nodes[x + 1][y].value == node.value:
                        node.neighbours.append(nodes[x + 1][y])
            if len(node.neighbours) == 4:
                x_min = min([n.x for n in node.neighbours])
                y_min = min([n.y for n in node.neighbours])
                x_max = max([n.x for n in node.neighbours])
                y_max = max([n.y for n in node.neighbours])
                vertices = 4
                if nodes[x_min][y_min].value == node.value:
                    vertices -= 1
                if nodes[x_min][y_max].value == node.value:
                    vertices -= 1
                if nodes[x_max][y_min].value == node.value:
                    vertices -= 1
                if nodes[x_max][y_max].value == node.value:
                    vertices -= 1
                node.vertices = vertices
            elif len(node.neighbours) == 3:
                min_x = node.x - 1
                min_y = node.y - 1
                max_x = node.x + 1
                max_y = node.y + 1
                if not (node.x, node.y - 1) in [(n.x, n.y) for n in node.neighbours]:
                    if node.y - 1 < 0:
                        vertices = 0
                        if not nodes[min_x][max_y].value == node.value:
                            vertices += 1
                        if not nodes[max_x][max_y].value == node.value:
                            vertices += 1
                    else:
                        vertices = 0
                        # if nodes[min_x][min_y].value == node.value:
                        #     vertices += 1
                        if not nodes[min_x][max_y].value == node.value:
                            vertices += 1
                        # if nodes[max_x][min_y].value == node.value:
                        #     vertices += 1
                        if not nodes[max_x][max_y].value == node.value:
                            vertices += 1
                elif not (node.x, node.y + 1) in [(n.x, n.y) for n in node.neighbours]:
                    if node.y + 1 >= len(row):
                        vertices = 0
                        if not nodes[min_x][min_y].value == node.value:
                            vertices += 1
                        if not nodes[max_x][min_y].value == node.value:
                            vertices += 1
                    else:
                        vertices = 0
                        if not nodes[min_x][min_y].value == node.value:
                            vertices += 1
                        # if nodes[min_x][max_y].value == node.value:
                        #     vertices += 1
                        if not nodes[max_x][min_y].value == node.value:
                            vertices += 1
                        # if nodes[max_x][max_y].value == node.value:
                        #     vertices += 1
                elif not (node.x - 1, node.y) in [(n.x, n.y) for n in node.neighbours]:
                    if node.x - 1 < 0:
                        vertices = 0
                        if not nodes[max_x][min_y].value == node.value:
                            vertices += 1
                        if not nodes[max_x][max_y].value == node.value:
                            vertices += 1
                    else:
                        vertices = 0
                        # if nodes[min_x][min_y].value == node.value:
                        #     vertices += 1
                        # if nodes[min_x][max_y].value == node.value:
                        #     vertices += 1
                        if not nodes[max_x][min_y].value == node.value:
                            vertices += 1
                        if not nodes[max_x][max_y].value == node.value:
                            vertices += 1
                else:
                    if node.x + 1 >= len(nodes):
                        vertices = 0
                        if not nodes[min_x][min_y].value == node.value:
                            vertices += 1
                        if not nodes[min_x][max_y].value == node.value:
                            vertices += 1
                    else:
                        vertices = 0
                        if not nodes[min_x][min_y].value == node.value:
                            vertices += 1
                        if not nodes[min_x][max_y].value == node.value:
                            vertices += 1
                        # if nodes[max_x][min_y].value == node.value:
                        #     vertices += 1
                        # if nodes[max_x][max_y].value == node.value:
                        #     vertices += 1
                node.vertices = vertices
            elif len(node.neighbours) == 2:
                n0 = node.neighbours[0]
                n1 = node.neighbours[1]
                if n0.x == n1.x or n0.y == n1.y:
                    node.vertices = 0
                else:
                    min_x = min(n0.x, n1.x, node.x)
                    min_y = min(n0.y, n1.y, node.y)
                    max_x = max(n0.x, n1.x, node.x)
                    max_y = max(n0.y, n1.y, node.y)
                    if (min_x, min_y) not in [(n0.x, n0.y), (n1.x, n1.y), (node.x, node.y)]:
                        x_empty = min_x
                        y_empty = min_y
                    elif (min_x, max_y) not in [(n0.x, n0.y), (n1.x, n1.y), (node.x, node.y)]:
                        x_empty = min_x
                        y_empty = max_y
                    elif (max_x, min_y) not in [(n0.x, n0.y), (n1.x, n1.y), (node.x, node.y)]:
                        x_empty = max_x
                        y_empty = min_y
                    else:
                        x_empty = max_x
                        y_empty = max_y
                    if not nodes[x_empty][y_empty].value == node.value:
                        node.vertices = 2
                    else:
                        node.vertices = 1
            elif len(node.neighbours) == 1:
                node.vertices = 2
            else:
                node.vertices = 4
    return nodes


def find_connected_components(graph: list[list[Node]]) -> list[list[Node]]:
    components = []
    for row in graph:
        for node in row:
            if node.visited:
                continue
            component = []
            stack = [node]
            while stack:
                current = stack.pop()
                if not current.visited:
                    component.append(current)
                    current.visited = True
                for neighbour in current.neighbours:
                    if not neighbour.visited:
                        stack.append(neighbour)
            components.append(component)
    return components


def find_component_prices(connected_components: list[list[Node]]) -> list[int]:
    prices = []
    for component in connected_components:
        area = len(component)
        vertices = 0
        for node in component:
            vertices += node.vertices
        price = area * vertices
        prices.append(price)
    return prices


if __name__ == '__main__':
    grid = []
    with open('input-a.txt', 'r') as f:
        for line in f:
            grid.append(line.strip())

    graph = create_graph(grid)
    # print(graph)
    connected_components = find_connected_components(graph)
    # print(connected_components)
    prices = find_component_prices(connected_components)
    print(prices)
    print(sum(prices))
