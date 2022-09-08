class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.adjacent = []  # List of Nodes this node points to

def has_route(start_node: GraphNode, end_node: GraphNode) -> bool:
    route = [start_node]
    already_visited = set()
    while route:
        node = route.pop(0)
        already_visited.add(node)
        if node == end_node:
            return True
        for neighbours in node.adjacent:
            if neighbours not in already_visited:
                route.append(neighbours)
    return False