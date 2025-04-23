# In this file, I demonstrate how to implement an undirected graph, and use breadth-first search to find a path from one node to another
# This is a modified version of the example from the Grokking Algorithms book, Chapter 6
# I originally made this version, but later realized that Grokking Algos was using a directed graph. 
# The Ch6Notes.py file uses a directed graph

from queue import Queue

# Implementing Graphs in Python
class Node:
    def __init__(self, name, mango_seller=False):
        self.name = name
        self.mango_seller = mango_seller
        self.neighbors = []
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

root.neighbors = [alice, bob, claire, shortcut]
bob.neighbors = [anuj, peggy, root]
alice.neighbors = [peggy, joe, root]
claire.neighbors = [root, thom, johny]
anuj.neighbors = [bob]
peggy.neighbors = [bob, burt, alice]
thom.neighbors = [claire]
johny.neighbors = [claire]
burt.neighbors = [peggy, target]
joe.neighbors = [alice, shane]
shane.neighbors = [tony, joe]
tony.neighbors = [shane, target]
target.neighbors = [tony, burt, shortcut]
shortcut.neighbors = [root, target]


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
                for neighbor in current.neighbors:
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