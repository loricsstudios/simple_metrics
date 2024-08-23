def two_color_graph(data):
    from collections import deque
    
    # Read the number of vertices and the edges
    num_vertices = data[0]
    edges = data[1]
    
    # Create adjacency list for the graph
    adjacency_list = [[] for _ in range(num_vertices)]
    for edge in edges:
        u, v = edge
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    
    # Initialize color array with -1 (uncolored)
    color = [-1] * num_vertices
    
    # Function to check if the graph can be colored using 2 colors starting from a given vertex
    def bfs_check(start):
        queue = deque([start])
        color[start] = 0  # Start coloring the starting vertex with color 0
        
        while queue:
            current = queue.popleft()
            current_color = color[current]
            
            for neighbor in adjacency_list[current]:
                if color[neighbor] == -1:  # If the neighbor has not been colored
                    color[neighbor] = 1 - current_color  # Assign the opposite color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:  # If the neighbor has the same color
                    return False
        return True
    
    # Check all components of the graph
    for vertex in range(num_vertices):
        if color[vertex] == -1:  # If this vertex has not been colored
            if not bfs_check(vertex):
                return []
    
    return color

# Example usage
# data = [11, [[2, 9], [6, 7], [5, 6], [8, 10], [3, 10], [4, 10], [3, 9], [1, 5], [4, 9], [3, 7], [0, 3], [0, 1], [1, 7], [0, 6], [2, 7], [6, 10], [4, 5], [1, 10], [7, 8]]]
# data = [4, [[0, 2], [0, 3], [1, 2], [1, 3]]]
# data = [3, [[0, 1], [0, 2], [1, 2]]]
data = [14,[[4,5],[3,7],[0,4],[2,4],[2,12],[3,4],[11,12],[5,9],[8,9],[11,13],[1,5],[5,9],[2,9],[1,3],[2,10],[4,11],[4,6],[5,7],[6,7],[0,10],[6,12],[0,9],[1,11],[3,12],[6,13]]]
print(two_color_graph(data))
