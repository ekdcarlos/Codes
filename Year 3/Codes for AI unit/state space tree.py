import networkx as nx
from collections import deque

# Define the state space
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

# Create a graph from the state space (not needed for search but kept for completeness)
G = nx.DiGraph()
for parent, children in state_space.items():
    for child in children:
        G.add_edge(parent, child)

# Search Algorithms
def dfs(graph, start):
    """Depth-First Search implementation"""
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))  # Reverse to maintain left-to-right order
    return visited

def bfs(graph, start):
    """Breadth-First Search implementation"""
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited

def dls(graph, node, depth, visited):
    """Depth-Limited Search (helper for IDS)"""
    if depth == 0:
        return [node]
    visited.append(node)
    for child in graph[node]:
        if child not in visited:
            visited += dls(graph, child, depth - 1, visited.copy())
    return visited

def ids(graph, start, max_depth):
    """Iterative Deepening Search implementation"""
    total_visited = []
    for depth in range(max_depth + 1):
        visited = dls(graph, start, depth, [])
        total_visited.extend(visited)
    # Remove duplicates while preserving order
    seen = set()
    return [x for x in total_visited if not (x in seen or seen.add(x))]

# Run searches and print results
print("DFS Order:", dfs(state_space, 'a'))
print("BFS Order:", bfs(state_space, 'a'))
print("IDS Order:", ids(state_space, 'a', 3))