# Implementation of Prim's and Kruskal's algorithms for Minimum Spanning Tree (MST)
# Includes a test harness to compare performance with example graphs

import heapq
import time
import random
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = defaultdict(list)  # Adjacency list for Prim's
        self.edges = []  # Edge list for Kruskal's

    def add_edge(self, u, v, weight):
        # Add edge for Prim's (undirected graph)
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))
        # Add edge for Kruskal's
        self.edges.append((weight, u, v))

# Union-Find data structure for Kruskal's algorithm
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        # Find the root of the set containing x with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Unite two sets by rank
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def prim_mst(graph):
    """Implements Prim's algorithm to find the Minimum Spanning Tree."""
    # Initialize variables
    visited = set()
    mst_edges = []
    total_weight = 0
    pq = []  # Priority queue for edges
    start_vertex = 0  # Start from vertex 0

    # Add edges from the starting vertex
    visited.add(start_vertex)
    for v, weight in graph.graph[start_vertex]:
        heapq.heappush(pq, (weight, start_vertex, v))

    # Continue until all vertices are visited or priority queue is empty
    while pq and len(visited) < graph.V:
        weight, u, v = heapq.heappop(pq)
        if v in visited:
            continue
        visited.add(v)
        mst_edges.append((u, v, weight))
        total_weight += weight

        # Add new edges from the newly visited vertex
        for next_v, next_weight in graph.graph[v]:
            if next_v not in visited:
                heapq.heappush(pq, (next_weight, v, next_v))

    return mst_edges, total_weight

def kruskal_mst(graph):
    """Implements Kruskal's algorithm to find the Minimum Spanning Tree."""
    # Sort edges by weight
    edges = sorted(graph.edges)
    uf = UnionFind(graph.V)
    mst_edges = []
    total_weight = 0

    # Process edges in increasing order of weight
    for weight, u, v in edges:
        if uf.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
        if len(mst_edges) == graph.V - 1:
            break

    return mst_edges, total_weight

def generate_random_graph(vertices, edge_density=0.5):
    """Generate a random connected graph with given number of vertices and edge density."""
    g = Graph(vertices)
    # Ensure the graph is connected by adding a chain
    for i in range(vertices - 1):
        weight = random.randint(1, 100)
        g.add_edge(i, i + 1, weight)

    # Add additional random edges based on density
    max_edges = (vertices * (vertices - 1)) // 2
    num_edges = int(max_edges * edge_density)
    for _ in range(num_edges - (vertices - 1)):
        u = random.randint(0, vertices - 1)
        v = random.randint(0, vertices - 1)
        if u != v and not any(v == x[0] for x in g.graph[u]):  # Avoid duplicate edges
            weight = random.randint(1, 100)
            g.add_edge(u, v, weight)
    return g

def run_performance_test(vertices_list, edge_density=0.5, trials=5):
    """Run performance tests for Prim's and Kruskal's algorithms."""
    print("Running performance tests...")
    print(f"Edge density: {edge_density}, Trials per size: {trials}")
    print("Vertices | Prim's Time (s) | Kruskal's Time (s) | Prim's Weight | Kruskal's Weight")
    print("-" * 70)

    for vertices in vertices_list:
        prim_times = []
        kruskal_times = []
        prim_weights = []
        kruskal_weights = []

        for _ in range(trials):
            g = generate_random_graph(vertices, edge_density)

            # Test Prim's algorithm
            start_time = time.time()
            _, prim_weight = prim_mst(g)
            prim_times.append(time.time() - start_time)
            prim_weights.append(prim_weight)

            # Test Kruskal's algorithm
            start_time = time.time()
            _, kruskal_weight = kruskal_mst(g)
            kruskal_times.append(time.time() - start_time)
            kruskal_weights.append(kruskal_weight)

        avg_prim_time = sum(prim_times) / trials
        avg_kruskal_time = sum(kruskal_times) / trials
        avg_prim_weight = sum(prim_weights) / trials
        avg_kruskal_weight = sum(kruskal_weights) / trials

        print(f"{vertices:8d} | {avg_prim_time:.6f} | {avg_kruskal_time:.6f} | {avg_prim_weight:.1f} | {avg_kruskal_weight:.1f}")

# Example usage and test cases
if __name__ == "__main__":
    # Example 1: Small graph
    print("Example 1: Small graph with 4 vertices")
    g1 = Graph(4)
    g1.add_edge(0, 1, 10)
    g1.add_edge(0, 2, 6)
    g1.add_edge(0, 3, 5)
    g1.add_edge(1, 3, 15)
    g1.add_edge(2, 3, 4)

    print("Prim's MST:", prim_mst(g1))
    print("Kruskal's MST:", kruskal_mst(g1))

    # Example 2: Another small graph
    print("\nExample 2: Small graph with 5 vertices")
    g2 = Graph(5)
    g2.add_edge(0, 1, 2)
    g2.add_edge(0, 3, 6)
    g2.add_edge(1, 2, 3)
    g2.add_edge(1, 3, 8)
    g2.add_edge(1, 4, 5)
    g2.add_edge(2, 4, 7)
    g2.add_edge(3, 4, 9)

    print("Prim's MST:", prim_mst(g2))
    print("Kruskal's MST:", kruskal_mst(g2))

    # Performance comparison
    print("\nPerformance Comparison:")
    vertices_list = [10, 50, 100, 500]  # Different graph sizes
    run_performance_test(vertices_list, edge_density=0.3, trials=5)