def Dijktra(graph, startnode):
    shortest_dist = {node:float('inf') for node in graph}
    shortest_dist[startnode] = 0
    visited  = set()
    print("===starting Disktra's Algorithm")
    while len(visited) < len(graph):
        unvisited_nodes = {node: dist for node,dist in shortest_dist.items() if node not in visited}
        current_node = min(unvisited_nodes, key = unvisited_nodes.get)
        current_dist  = shortest_dist[current_node]
        print("Visiting node:{current_node},current.shortest_dist:{current_dist}")
        for neighbor, weight  in graph[current_node].items():
            if neighbor not in visited:
                new_distance = current_dist + weight
                print(f"Checking neighbor: {neighbor}, edge weight: {weight}, new distance: {new_distance}")
                if new_distance < shortest_dist[neighbor]:
                    shortest_dist[neighbor] = new_distance 
                    print(f"updating the path for {neighbor} to {new_distance}")
                    visited.add(current_node)
                    for node, dist  in shortest_dist.items():
                        print(f"-{node}:{dist}")
        return shortest_dist
graph = {'A':{'B':4,'D':8},
         'B':{'A':4,'C':6},
         'C':{'B':6,'D':1},
         'D':{'A':8,'C':1},
         'E':{'C':5}}
Dijktra(graph, 'A')