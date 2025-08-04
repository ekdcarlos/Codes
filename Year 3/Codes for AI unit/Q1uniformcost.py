import heapq

def uniform_cost_search(graph, start, goal):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))  # (cumulative_cost, node, path)

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        
        if node == goal:
            return path, cost
        
        if node not in visited:
            visited.add(node)
            
            for neighbor, edge_cost in graph[node].items():
                if neighbor not in visited:
                    new_cost = cost + edge_cost
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (new_cost, neighbor, new_path))
    
    return None, float('inf')  # No path found

# Example Usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

path, cost = uniform_cost_search(graph, 'A', 'D')
print(f"Optimal Path: {path}")
print(f"Total Cost: {cost}")