from collections import defaultdict

class Graph:
    #Constructor
    def __init__(self):
        #default dictionary to store graph
        self.graph = defaultdict(list)

    #Function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
        

    #Function to print a BFS of a graph
    def BFS(self, s):
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
        # Create a queue for BFS
        queue = []
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end=" ")
            # Get all adjacent vertices of the dequeued vertex s. If an adjacent has not been visited, mark it visited and enqueue it

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
#Driver code
#create a graph given in the above diagram
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is Breadth First Traversal (starting from vertex 2)")
g.BFS(2)  # Starting BFS from vertex 2