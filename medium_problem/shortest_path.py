# Import deque from collections module for efficient queue operations
from collections import deque

# Define a class named 'graph' to represent an undirected/directed graph
class graph:
    
    # Constructor to initialize an empty dictionary for storing adjacency lists
    def __init__(self):
        self.graph = {}
        
    # Function to add an edge between two nodes (u, v)
    def add_edge(self, u, v, directed = False):
        
        # If node u is not in the graph, initialize it with an empty list
        if u not in self.graph:
            self.graph[u] = []
            
        # Add node v to u’s adjacency list
        self.graph[u].append(v)
        
        # If the graph is undirected, also add u to v’s adjacency list
        if not directed:
            if v not in self.graph:
                self.graph[v] = []
                
            self.graph[v].append(u)
            
    # Function to find the shortest path distance from a starting node using BFS
    def shortest_path(self, start):
        # Initialize all distances as infinity
        dist = {node: float('inf') for node in self.graph}
        # Distance to the start node is 0
        dist[start] = 0
        
        # Initialize a queue and enqueue the starting node
        q = deque([start])
        
        # Perform BFS traversal
        while q:
            # Pop a node from the front of the queue
            node = q.popleft()
            
            # Visit all its neighbors
            for neighbour in self.graph[node]:
                # If the neighbor hasn't been visited (distance is infinity)
                if dist[neighbour] == float('inf'):
                    # Update the distance of the neighbor
                    dist[neighbour] = dist[node] + 1
                    # Enqueue the neighbor for further traversal
                    q.append(neighbour)
                    
        # Return the dictionary containing shortest distances from the start node
        return dist

# Create a graph object
g = graph()
# Add edges between nodes
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)

# Define the starting node
start = 0
# Call shortest_path to compute distances from the start node
res = g.shortest_path(0)
# Print the result (shortest distance to all nodes)
print(res)
