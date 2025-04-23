# In this file, I will implement an AVL tree, which is a self-balancing binary search tree
# It will need nodes, which have a value, a left child, and a right child, a height, and a balance factor
# We will be able to insert, delete, and search for values in the tree
# I will also make a function to print out the tree in a readable format

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def getHeight(node):
    if node is None:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.right) - getHeight(node.left)


def rightRotate(y):
    print(f"Right Rotate on node ['{y.value}']")
    
    # Set Pointers
    x = y.left
    T2 = x.right

    # Rotate
    x.right = y
    y.left = T2

    # Update Heights
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))

    return x


def leftRotate(x):
    print(f"Left Rotate on node ['{x.value}']")
    
    # Set Pointers
    y = x.right
    T2 = y.left

    # Rotate
    y.left = x
    x.right = T2

    # Update Heights
    x.height = 1 + max(getHeight(x.left), getHeight(x.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))

    return y

def insert(node, value):
    
    # Base Case
    if node is None:
        return Node(value)
    
    # Pass the value down the tree, it will eventually reach the bottom of the tree in its correct position (see base case)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)

    # Now that the value has been inserted, we need to update the height, check the balance factor, and rotate if necessary

    node.height = 1 + max(getHeight(node.left), getHeight(node.right))
    balance = getBalance(node)

    # Left Left Case
    if balance < -1 and getBalance(node.left) < 0:
        return rightRotate(node)
    
    # Right Right Case
    if balance > 1 and getBalance(node.right) > 0:
        return leftRotate(node)
    
    # Left Right Case
    if balance < -1 and getBalance(node.left) > 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    
    # Right Left Case
    if balance > 1 and getBalance(node.right) < 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node


def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print('  ' * level, node.value)
        printTree(node.left, level + 1)



root = None
root = insert(root, 10)
root = insert(root, 20)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 25)

printTree(root)