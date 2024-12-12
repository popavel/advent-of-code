class Node:
    def __init__(self, x: int, y: int, value: str):
        self.x = x
        self.y = y
        self.value = value
        self.neighbours = []
        self.perimeter = 0
        self.visited = False

    def __str__(self):
        return f'Node({self.x}, {self.y}, {self.value}, perimeter: {self.perimeter}, neighbours: {[(n.x, n.y) for n in self.neighbours]})'

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
            perimeter = 4
            if x == 0:
                if y == 0:
                    if nodes[x][y + 1].value == node.value:
                        node.neighbours.append(nodes[x][y + 1])
                        perimeter -= 1
                    if nodes[x + 1][y].value == node.value:
                        node.neighbours.append(nodes[x + 1][y])
                        perimeter -= 1
                elif y == len(row) - 1:
                    if nodes[x][y - 1].value == node.value:
                        node.neighbours.append(nodes[x][y - 1])
                        perimeter -= 1
                    if nodes[x + 1][y].value == node.value:
                        node.neighbours.append(nodes[x + 1][y])
                        perimeter -= 1
                else:
                    if nodes[x][y - 1].value == node.value:
                        node.neighbours.append(nodes[x][y - 1])
                        perimeter -= 1
                    if nodes[x][y + 1].value == node.value:
                        node.neighbours.append(nodes[x][y + 1])
                        perimeter -= 1
                    if nodes[x + 1][y].value == node.value:
                        node.neighbours.append(nodes[x + 1][y])
                        perimeter -= 1
            elif x == len(nodes) - 1:
                if y == 0:
                    if nodes[x][y + 1].value == node.value:
                        node.neighbours.append(nodes[x][y + 1])
                        perimeter -= 1
                    if nodes[x - 1][y].value == node.value:
                        node.neighbours.append(nodes[x - 1][y])
                        perimeter -= 1
                elif y == len(row) - 1:
                    if nodes[x][y - 1].value == node.value:
                        node.neighbours.append(nodes[x][y - 1])
                        perimeter -= 1
                    if nodes[x - 1][y].value == node.value:
                        node.neighbours.append(nodes[x - 1][y])
                        perimeter -= 1
                else:
                    if nodes[x][y - 1].value == node.value:
                        node.neighbours.append(nodes[x][y - 1])
                        perimeter -= 1
                    if nodes[x][y + 1].value == node.value:
                        node.neighbours.append(nodes[x][y + 1])
                        perimeter -= 1
                    if nodes[x - 1][y].value == node.value:
                        node.neighbours.append(nodes[x - 1][y])
                        perimeter -= 1
            else:
                if y == 0:
                    if nodes[x][y + 1].value == node.value:
                        node.neighbours.append(nodes[x][y + 1])
                        perimeter -= 1
                    if nodes[x - 1][y].value == node.value:
                        node.neighbours.append(nodes[x - 1][y])
                        perimeter -= 1
                    if nodes[x + 1][y].value == node.value:
                        node.neighbours.append(nodes[x + 1][y])
                        perimeter -= 1
                elif y == len(row) - 1:
                    if nodes[x][y - 1].value == node.value:
                        node.neighbours.append(nodes[x][y - 1])
                        perimeter -= 1
                    if nodes[x - 1][y].value == node.value:
                        node.neighbours.append(nodes[x - 1][y])
                        perimeter -= 1
                    if nodes[x + 1][y].value == node.value:
                        node.neighbours.append(nodes[x + 1][y])
                        perimeter -= 1
                else:
                    if nodes[x][y - 1].value == node.value:
                        node.neighbours.append(nodes[x][y - 1])
                        perimeter -= 1
                    if nodes[x][y + 1].value == node.value:
                        node.neighbours.append(nodes[x][y + 1])
                        perimeter -= 1
                    if nodes[x - 1][y].value == node.value:
                        node.neighbours.append(nodes[x - 1][y])
                        perimeter -= 1
                    if nodes[x + 1][y].value == node.value:
                        node.neighbours.append(nodes[x + 1][y])
                        perimeter -= 1
            node.perimeter = perimeter
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
        perimeter = 0
        for node in component:
            perimeter += node.perimeter
        price = area * perimeter
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
    # print(prices)
    print(sum(prices))
