import networkx as nx
import itertools
import time

# Define the graph with ore information (including value and weight) and edges (including distance)
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

# Add edges with travel jarak (consider both directions)
edges = [
    ('A', 'B', 5), ('B', 'A', 5), ('A', 'H', 6), ('H', 'A', 6),
    ('A', 'C', 3), ('C', 'A', 3), ('B', 'D', 4), ('D', 'B', 4),
    ('B', 'E', 7), ('E', 'B', 7), ('C', 'E', 6), ('E', 'C', 6),
    ('D', 'F', 5), ('F', 'D', 5), ('E', 'G', 8), ('G', 'E', 8),
    ('H', 'B', 2), ('B', 'H', 2), ('H', 'I', 4), ('I', 'H', 4),
    ('C', 'H', 3), ('H', 'C', 3), ('E', 'I', 4), ('I', 'E', 4),
    ('I', 'F', 10), ('F', 'I', 10), ('G', 'F', 8), ('F', 'G', 10)
]
for u, v, jarak in edges:
    G.add_edge(u, v, jarak=jarak)

MAX_ORE_WEIGHT = 15  # Maximum weight the miner can carry

def brute_force_solution(graph, max_ore_weight):
    best_path = []
    best_value = 0
    best_ore_weight = 0
    best_total_distance = 0
    best_ore_counts = {}

    nodes = list(graph.nodes())
    nodes.remove('A')

    # Generate all possible paths that start and end at 'A'
    for length in range(1, len(nodes) + 1):  # Length starts from 1 to ensure visiting at least one other node
        for subset in itertools.permutations(nodes, length):
            path = ['A'] + list(subset) + ['A']
            total_value = 0
            total_ore_weight = 0
            total_distance = 0
            ore_counts = {}

            # Evaluate the path
            valid_path = True
            for i in range(len(path) - 1):
                if not graph.has_edge(path[i], path[i + 1]):
                    valid_path = False
                    break

            if not valid_path:
                continue

            for i in range(1, len(path) - 1):  # Skip the first and last 'A'
                node = path[i]
                total_value += graph.nodes[node]['value']
                total_ore_weight += graph.nodes[node]['weight']
                ore_counts[graph.nodes[node]['ore']] = ore_counts.get(graph.nodes[node]['ore'], 0) + 1

            for i in range(len(path) - 1):
                total_distance += graph.edges[path[i], path[i + 1]]['jarak']

            if total_ore_weight <= max_ore_weight and (total_value > best_value or (total_value == best_value and total_distance < best_total_distance)):
                best_path = path
                best_value = total_value
                best_ore_weight = total_ore_weight
                best_total_distance = total_distance
                best_ore_counts = ore_counts.copy()

    return best_path, best_value, best_ore_weight, best_total_distance, best_ore_counts

def measure_running_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    running_time = end_time - start_time
    return result, running_time

# Measure the running time of brute force solution
(brute_force_path, brute_force_value, brute_force_ore_weight, brute_force_total_distance, brute_force_ore_counts), brute_force_running_time = measure_running_time(brute_force_solution, G, MAX_ORE_WEIGHT)

print("Brute Force Solution:")
print(f"Best Path: {brute_force_path}")
print(f"Total Value: {brute_force_value}")
print(f"Total Weight: {brute_force_ore_weight}")
print(f"Ore: {brute_force_ore_counts}")
print(f"Total Distance: {brute_force_total_distance}")
print(f"Running Time: {brute_force_running_time:.6f} seconds")
