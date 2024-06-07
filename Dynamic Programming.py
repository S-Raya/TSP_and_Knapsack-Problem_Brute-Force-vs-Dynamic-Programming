import networkx as nx
import time

# Define the graph with ore information (including weight and value) and edges (including distance)
G = nx.DiGraph()

# Add nodes with ore information (including weight and value)
G.add_node('A', ore='start', value=0, weight=0)
G.add_node('B', ore='iron', value=6, weight=2)
G.add_node('C', ore='coal', value=2, weight=1)
G.add_node('D', ore='gold', value=8, weight=5)
G.add_node('E', ore='gold', value=8, weight=5)
G.add_node('F', ore='diamond', value=12, weight=7)
G.add_node('G', ore='iron', value=6, weight=2)
G.add_node('H', ore='coal', value=2, weight=1)
G.add_node('I', ore='diamond', value=12, weight=7)

# Add edges with travel distance (consider both directions)
edges = [
    ('A', 'B', 5), ('B', 'A', 5), ('A', 'H', 6), ('H', 'A', 6),
    ('A', 'C', 3), ('C', 'A', 3), ('B', 'D', 4), ('D', 'B', 4),
    ('B', 'E', 7), ('E', 'B', 7), ('C', 'E', 6), ('E', 'C', 6),
    ('D', 'F', 5), ('F', 'D', 5), ('E', 'G', 8), ('G', 'E', 8),
    ('H', 'B', 2), ('B', 'H', 2), ('H', 'I', 4), ('I', 'H', 4),
    ('C', 'H', 3), ('H', 'C', 3), ('E', 'I', 4), ('I', 'E', 4),
    ('I', 'F', 10), ('F', 'I', 10), ('G', 'F', 8), ('F', 'G', 10)
]
for u, v, distance in edges:
    G.add_edge(u, v, distance=distance)

MAX_ORE_WEIGHT = 15  # Maximum weight the miner can carry

def dynamic_programming_solution(graph, max_ore_weight):
    # Memoization table
    memo = {}

    def dp(node, carried_weight, visited):
        if (node, carried_weight, tuple(sorted(visited))) in memo:
            return memo[(node, carried_weight, tuple(sorted(visited)))]

        best_value = 0
        best_weight = 0
        best_path = [node]

        for neighbor in graph.successors(node):
            edge_distance = graph.edges[node, neighbor]['distance']
            ore_weight = graph.nodes[neighbor]['weight']
            ore_value = graph.nodes[neighbor]['value']

            if carried_weight + ore_weight <= max_ore_weight:
                if neighbor not in visited:
                    new_visited = visited.copy()
                    new_visited.add(neighbor)
                    neighbor_value, neighbor_weight, neighbor_path = dp(neighbor, carried_weight + ore_weight, new_visited)
                    total_value = ore_value + neighbor_value
                    total_weight = ore_weight + neighbor_weight

                    if total_value > best_value or (total_value == best_value and total_weight < best_weight):
                        best_value = total_value
                        best_weight = total_weight
                        best_path = [node] + neighbor_path

        memo[(node, carried_weight, tuple(sorted(visited)))] = (best_value, best_weight, best_path)
        return memo[(node, carried_weight, tuple(sorted(visited)))]

    # Ensure that the miner starts at 'A', goes to at least one other node, and returns to 'A'
    best_value, best_weight, best_path = dp('A', 0, set(['A']))

    # Ensure the path starts and ends at 'A'
    if best_path and best_path[-1] != 'A':
        best_path.append('A')

    # Ensure the miner moves to at least one node
    if len(best_path) == 2 and best_path[0] == best_path[1] == 'A':
        best_path = []

    return best_path, best_value, best_weight

# Measure the running time
start_time = time.time()
dp_path, dp_value, dp_weight = dynamic_programming_solution(G, MAX_ORE_WEIGHT)
end_time = time.time()
running_time = end_time - start_time

# Calculate ore counts and total distance
ore_counts = {}
total_distance = 0
for i in range(len(dp_path) - 1):
    ore = G.nodes[dp_path[i]]['ore']
    if ore != 'start':
        ore_counts[ore] = ore_counts.get(ore, 0) + 1
    total_distance += G.edges[dp_path[i], dp_path[i + 1]]['distance']

# Include the ore from the last node if it's not 'start'
if dp_path and G.nodes[dp_path[-1]]['ore'] != 'start':
    ore = G.nodes[dp_path[-1]]['ore']
    ore_counts[ore] = ore_counts.get(ore, 0) + 1

print("Dynamic Programming Solution:")
print(f"Best Path: {dp_path}")
print(f"Total Value: {dp_value}")
print(f"Total Weight: {dp_weight}")
print(f"Ore: {ore_counts}")
print(f"Total Distance: {total_distance}")
print(f"Running Time: {running_time:.6f} seconds")
