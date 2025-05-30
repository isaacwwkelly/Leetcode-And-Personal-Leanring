# Breadth First Search is good for finding the shortest path between two nodes, if the graph is unweighted.
# Shortest path means least number of edges, or steps.
# To see it in action, run it once, see the result, then comment out all references to shortcut, and run it again.

from queue import Queue

# Implementing Graphs in Python
class Node:
    def __init__(self, name, mango_seller=False):
        self.name = name
        self.mango_seller = mango_seller
        self.out_neighbors = []
        self.path_from_root = []

root = Node("Root")
bob = Node("Bob")
alice = Node("Alice")
claire = Node("Claire")
anuj = Node("Anuj")
peggy = Node("Peggy")
thom = Node("Thom")
johny = Node("Johny")
burt = Node("Burt")
joe = Node("Joe")
shane = Node("Shane")
tony = Node("Tony")
target = Node("Target", True)
shortcut = Node("Shortcut")

root.out_neighbors = [alice, bob, claire, shortcut]
bob.out_neighbors = [anuj, peggy]
alice.out_neighbors = [peggy, joe]
claire.out_neighbors = [thom, johny]
anuj.out_neighbors = []
peggy.out_neighbors = [burt]
thom.out_neighbors = []
johny.out_neighbors = []
burt.out_neighbors = [target]
joe.out_neighbors = [shane]
shane.out_neighbors = [tony]
tony.out_neighbors = [target]
target.out_neighbors = []
shortcut.out_neighbors = [target]


# Breadth First Search
# Time complexity: O(V + E) where V is the number of vertices and E is the number of edges
def BreadthFirstSearch(root):
    queue = Queue()
    queue.put(root)
    visited = set()
    added_to_queue = set()
    while not queue.empty():
        current = queue.get()
        # print(f"Evaluating {current.name}... They are {'not ' if not current.mango_seller else ''}a mango seller.")
        if current not in visited:    
            if current.mango_seller:
                return (current.name, current.path_from_root)
            else:
                for neighbor in current.out_neighbors:
                    if neighbor in visited:
                        continue

                    if neighbor not in added_to_queue:
                        added_to_queue.add(neighbor)
                        # Add the neighbor to the queue
                        queue.put(neighbor)
                    
                    # Update that neighbor's path_from_root
                    if neighbor.path_from_root == []:
                        neighbor.path_from_root = current.path_from_root + [current.name]
                visited.add(current)

    return (None, None)

result = BreadthFirstSearch(root)
if result[0] == None:
    print("No mango seller found")
else:
    print(f"BreadthFirstSearch(root) --> [{result[0]}] is a mango seller | length from root: {len(result[1])}, path from root: {' -> '.join(result[1] + [result[0]])}")