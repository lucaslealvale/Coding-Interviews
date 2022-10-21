# Do not modify the classes below
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, representation: str):
        '''
        representation: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        if not representation:
            return
        nodes = []
        for i, value in enumerate(representation):
            node = None
            if value is not None:
                node = TreeNode(value)
                if i > 0:
                    if i % 2 == 1:
                        parent = nodes[(i - 1) // 2]
                        parent.left = node
                    else:
                        parent = nodes[(i - 2) // 2]
                        parent.right = node
            nodes.append(node)
        self.root = nodes[0]


class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.adjacent = []


class Graph:
    def __init__(self, adjacency: list[list[bool]]):
        '''
        adjacency: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        self.nodes = [GraphNode(i) for i in range(1, len(adjacency) + 1)]
        for node1, row in zip(self.nodes, adjacency):
            for node2, adjacent in zip(self.nodes, row):
                if adjacent and node1 is not node2:
                    node1.adjacent.append(node2)


# Implement the functions below

def pre_order_recursive(root: TreeNode) -> None:
    
    if root == None:
        return
    
    print(root.value)
    
    pre_order_recursive(root.left)

    pre_order_recursive(root.right)

    pass


def pre_order_iterative(root: TreeNode) -> None:
    
    lista = []
    lista.append(root)

    while(len(lista)>0):
        
        root = lista.pop()
        
        print(root.value)
        
        if root.right:
            lista.append(root.right)
        
        if root.left:
            lista.append(root.left)


def in_order_recursive(root: TreeNode) -> None:

    if root == None:
        return
    
    in_order_recursive(root.left)

    print(root.value)
    
    in_order_recursive(root.right)


def post_order_recursive(root: TreeNode) -> None:
   
    if root == None:
        return

    post_order_recursive(root.left)
    
    post_order_recursive(root.right)
    
    print(root.value)

def breadth_first(root: TreeNode) -> None:
    
    already_visited = []
    already_visited.append(root)

    while already_visited:
        node = already_visited.pop(0)
        
        print(node.value)

        if node.left != None:
            already_visited.append(node.left)
            
        if node.right != None:
            already_visited.append(node.right)
    


def graph_depth_first_recursive(node: GraphNode, visited=None) -> None:
    if visited is None:
        visited = set()
    # Your code goes here
    visited.add(node)
    print(node.value)
    for neighbour in node.adjacent:
        if neighbour not in visited:
            graph_depth_first_recursive(neighbour, visited)


def graph_depth_first_iterative(node: GraphNode) -> None:
    visited = []	
    visited.append(node)
    
    setNode = set()
    setNode.add(node)

    while len(visited) != 0:
        node2 = visited.pop()
        print(node2.value)
        
        for neighbour in node2.adjacent:
            if neighbour not in setNode:
                setNode.add(neighbour)
                visited.append(neighbour)
    
    

def graph_breadth_first(node: GraphNode) -> None:

    route = [node]
    already_visited = set()
    already_visited.add(node)
    
    while len(route)>0:
        node = route.pop(0)

        print(node.value)

        for neighbours in node.adjacent:
            if neighbours not in already_visited:
                route.append(neighbours)
                already_visited.add(neighbours)

    