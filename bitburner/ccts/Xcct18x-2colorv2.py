from collections import deque

def two_color_graph(data):
    num_vertices = data[0]
    edges = data[1]
    
    # Step 1: Build the adjacency list
    adj_list = [[] for _ in range(num_vertices)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # Step 2: Initialize color array
    colors = [-1] * num_vertices
    
    # Step 3: BFS to color the graph
    def bfs(start):
        queue = deque([start])
        colors[start] = 0  # Start coloring with 0
        
        while queue:
            node = queue.popleft()
            current_color = colors[node]
            
            for neighbor in adj_list[node]:
                if colors[neighbor] == -1:  # If not colored, color it with alternate color
                    colors[neighbor] = 1 - current_color
                    queue.append(neighbor)
                elif colors[neighbor] == current_color:  # If the same color as current node, not bipartite
                    return False
        return True
    
    # Try to color each component of the graph
    for vertex in range(num_vertices):
        if colors[vertex] == -1:  # If not yet colored
            if not bfs(vertex):
                return []
    
    return colors

# Given data
data = [12,[[1,6],[7,9],[2,5],[0,5],[2,3],[6,9],[0,3],[1,8],[0,7],[2,11],[10,11],[2,6],[1,3],[1,7],[2,4],[4,10],[3,9],[0,8],[1,5],[9,11],[0,11],[5,10],[6,10],[1,11],[3,6]]]

# Get the 2-coloring of the graph
result = two_color_graph(data)
print(result)
