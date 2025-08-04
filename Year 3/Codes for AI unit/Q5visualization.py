import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Define the state space as a dictionary where keys are parent nodes 
# and values are lists of child nodes

state_space = {
    'a': ['c', 'b','g','e'],
    'c': ['p', 'd','h'],
    'b': ['d'],
    'e': ['g','n', 'm'],
    'p': [],
    'd': ['h','f'],
    'g': [ 'o'],
    'n': ['k','o'],
    'm': [],
    'h': [],
    'f': [],
    'o': [],
    'k': []
}


# Create a directed graph from the state space
G = nx.DiGraph()
for parent, children in state_space.items():
    for child in children:
        G.add_edge(parent, child)  # Add edges from parent to each child

# Depth-First Search (DFS) implementation
def dfs(graph, start):
    visited = []        # Track visited nodes
    stack = [start]     # Use stack for DFS (LIFO)
    
    while stack:
        node = stack.pop()  # Get the last node from stack
        if node not in visited:
            visited.append(node)
            # Add children in reverse order to maintain left-to-right exploration
            stack.extend(reversed(graph[node]))
    return visited

# Breadth-First Search (BFS) implementation
def bfs(graph, start):
    visited = []        # Track visited nodes
    queue = deque([start])  # Use queue for BFS (FIFO)
    
    while queue:
        node = queue.popleft()  # Get the first node from queue
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])  # Add children in order
    return visited

# Depth-Limited Search (helper for IDS)
def dls(graph, node, depth, visited):
    if depth == 0:      # Base case: reached depth limit
        return [node]
    visited.append(node)
    for child in graph[node]:
        if child not in visited:
            # Recursively search with reduced depth
            visited += dls(graph, child, depth - 1, visited.copy())
    return visited

# Iterative Deepening Search (IDS) implementation
def ids(graph, start, max_depth):
    total_visited = []
    for depth in range(max_depth + 1):  # Gradually increase depth
        visited = dls(graph, start, depth, [])
        total_visited.extend(visited)
    # Remove duplicates while preserving order
    seen = set()
    return [x for x in total_visited if not (x in seen or seen.add(x))]

# Run searches and store results
dfs_order = dfs(state_space, 'a')
bfs_order = bfs(state_space, 'a')
ids_order = ids(state_space, 'a', 3)  # Max depth of 3 for IDS

# Visualization function using pydot
def visualize_search(graph, order, title):
    plt.figure(figsize=(10, 8))
    
    # Generate hierarchical layout using pydot
    try:
        pos = nx.nx_pydot.graphviz_layout(graph, prog='dot')
    except:
        # Fallback to spring layout if pydot fails
        pos = nx.spring_layout(graph)
    
    # Draw the complete graph
    nx.draw_networkx_nodes(graph, pos, node_size=1200, 
                          node_color='lightblue', alpha=0.9)
    nx.draw_networkx_edges(graph, pos, arrowstyle='->', 
                          arrowsize=20, width=2)
    nx.draw_networkx_labels(graph, pos, font_size=14, 
                          font_weight='bold')
    
    # Animate the search path
    for i, node in enumerate(order):
        plt.title(f"{title}\nStep {i+1}: Visiting {node}", 
                fontsize=16, pad=20)
        # Highlight the current node
        nx.draw_networkx_nodes(graph, pos, nodelist=[node], 
                             node_size=1200, node_color='red')
        plt.pause(1.5)  # Pause for 1.5 seconds between steps
        plt.draw()      # Update the visualization
    
    plt.show(block=False)

# Visualize each search algorithm
print("DFS Order:", dfs_order)
visualize_search(G, dfs_order, "Depth-First Search (DFS)")

print("\nBFS Order:", bfs_order)
visualize_search(G, bfs_order, "Breadth-First Search (BFS)")

print("\nIDS Order:", ids_order)
visualize_search(G, ids_order, "Iterative Deepening Search (IDS)")

plt.show()  # Keep all windows open