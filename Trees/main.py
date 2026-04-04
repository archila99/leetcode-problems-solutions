# Node structure for tree
class Node:
    def __init__(self, x):
        self.data = x
        self.children = []

# Function to add a child to a node
def addChild(parent, child):
    parent.children.append(child)


# Function to print a parents of each node
def prinParents(node, parent):
    if parent is None:
        print(str(node.data) + "-> NULL")
    else:
        print(str(node.data) + "-> " + str(parent.data))
    
    for child in node.children:
        prinParents(child, node)

# Function to print children of each node
def printChildren(node):
    children_str = " ".join(str(child.data) for child in node.children)
    print(str(node.data) + " ->" + children_str)
    for child in node.children:
        printChildren(child)
    

