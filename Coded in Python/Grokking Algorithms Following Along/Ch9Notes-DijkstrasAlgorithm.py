# In this file, I will demonstrate how to implement Dijkstra's algorithm, which finds the fastest (or lightest) path in a weighted graph.
# For the graph, it will be weighted and directed. This means each edge has a value (weight), and a node's neighbors will be 'out-neighbors'.

# Initialize the graph
# graph is a hash table, and it's keys are nodes
# at graph[node], there is a sub hash table, and it's keys are out neighbors. The values are the weights between the node and the out neighbor
# So the value at graph["start"]["a"] is the weight between start and a, which in this case is 6


# There is a more efficient version of this algo that uses a priority queue. I will implement that later

import math

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# Initialize the costs dictionary
# This will first have all values set to infinity, then it will set the cost of any out neighbor of the starting node.
# In dijkstra(), the other nodes will be processsed in order and their costs will be updated there.
infinity = math.inf
costs = {}
def initialize_costs(starting_node_key):
    keys = [x for x in graph.keys() if x != starting_node_key]
    for key in keys:
        costs[key] = infinity
    for key in graph[starting_node_key].keys():
        costs[key] = graph[starting_node_key][key]


# Initialize the parents dictionary
parents = {}
def initialize_parents(starting_node_key, target_node_key):
    for key in graph[starting_node_key].keys():
        parents[key] = starting_node_key
    parents[target_node_key] = None


# Initialize the processed set
processed = set() # This keeps track of the nodes that have already been processed. In Dijkstra's Algo, we only need to process each node once.

# This function returns the next node to process.
# It will be the node with the lowest cost that hasn't been processed yet.
def find_lowest_cost_node():
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Dijkstra's Algorithm
def dijkstra(starting_node_key, target_node_key):
    
    initialize_costs(starting_node_key)
    initialize_parents(starting_node_key, target_node_key)
    
    # grab the node that is closest to the start\
    node = find_lowest_cost_node()

    # while we have nodes to process
    while node is not None:
        
        cost = costs[node]
        neighbors = graph[node]
        
        # if needed, update the costs and parents for its neighbors
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node

        # mark the node as processed
        processed.add(node)

        # grab the next node
        node = find_lowest_cost_node()


# Once dijkstra() runs, costs{} and parents{} will have been updated to reflect the shortest paths from start to target
# We can then use the parents{} dictionary to trace the shortest path from start to target
def trace_shortest_path(starting_node_key, target_node_key):
    path = [target_node_key]
    while target_node_key != starting_node_key:
        target_node_key = parents[target_node_key]
        path.append(target_node_key)
    return path[::-1]




find_dijkstra_path = dijkstra("start", "fin")
path = trace_shortest_path("start", "fin")

print(f"The shortest path from start to fin is: [{' -> '.join(path)}], which has a cost of {costs['fin']}")
