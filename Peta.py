import networkx as nx
import matplotlib.pyplot as plt

# Membuat Graf
G = nx.Graph()

# Membuat node dengan ore, value, dan weight
G.add_node('A', ore= 'start', value=0, weight=0)
G.add_node('B', ore='iron', value=6, weight=2)
G.add_node('C', ore='coal', value=2, weight=1)
G.add_node('D', ore='gold', value=8, weight=5)
G.add_node('E', ore='gold', value=8, weight=5)
G.add_node('F', ore='diamond', value=12, weight=7)
G.add_node('G', ore='iron', value=6, weight=2)
G.add_node('H', ore='coal', value=2, weight=1)
G.add_node('I', ore='diamond', value=12, weight=7)

# Membuat edge dua arah dengan jaraknya
G.add_edge('A', 'B', jarak=5)
G.add_edge('B', 'A', jarak=5)  
G.add_edge('A', 'H', jarak=6)
G.add_edge('H', 'A', jarak=6)  
G.add_edge('A', 'C', jarak=3)
G.add_edge('C', 'A', jarak=3)  
G.add_edge('B', 'D', jarak=4)
G.add_edge('D', 'B', jarak=4)  
G.add_edge('B', 'E', jarak=7)
G.add_edge('E', 'B', jarak=7)  
G.add_edge('C', 'E', jarak=6)
G.add_edge('E', 'C', jarak=6) 
G.add_edge('D', 'F', jarak=5)
G.add_edge('F', 'D', jarak=5)  
G.add_edge('E', 'G', jarak=8)
G.add_edge('G', 'E', jarak=8)  
G.add_edge('H', 'B', jarak=2)
G.add_edge('B', 'H', jarak=2)  
G.add_edge('H', 'I', jarak=4)
G.add_edge('I', 'H', jarak=4)  
G.add_edge('C', 'H', jarak=3)
G.add_edge('H', 'C', jarak=3)  
G.add_edge('E', 'I', jarak=4)
G.add_edge('I', 'E', jarak=4)  
G.add_edge('I', 'A', jarak=7)
G.add_edge('A', 'I', jarak=7)  
G.add_edge('I', 'F', jarak=10)
G.add_edge('F', 'I', jarak=10)  
G.add_edge('G', 'F', jarak=8)
G.add_edge('F', 'G', jarak=8)  

# Posisi node
pos = {
  'A': (0, 0),
  'B': (1, 2),
  'C': (1, -2),
  'D': (2, 3),
  'E': (2, -3),
  'F': (3, 4),
  'G': (3, -4),
  'H': (1, 0),
  'I': (2, 0),
}

# Menambahkan Warna
ore_colors = {
  'start':'green',
  'coal': 'red',
  'iron': 'silver',
  'gold': 'yellow',
  'diamond': 'lightblue'
}

# Menggambar graf
nx.draw(G, pos, with_labels=True, node_size=700, node_color=[ore_colors[node_data['ore']] for node, node_data in G.nodes(data=True)], font_size=10, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'jarak')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Print Informasi Node
print("Nodes and their attributes:")
for node, node_data in G.nodes(data=True):
    print(f"Node: {node} - Ore: {node_data['ore']}, Value: {node_data['value']}, Weight: {node_data['weight']}")

print("\nEdges and their weights:")
for edge in G.edges(data=True):
    print(edge)

plt.show()