def can_two_color(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    colors = [-1] * n  # -1 means uncolored

    def dfs(node, color):
        if colors[node] != -1:
            return colors[node] == color
        colors[node] = color
        for neighbor in graph[node]:
            if not dfs(neighbor, 1 - color):
                return False
        return True

    for i in range(n):
        if colors[i] == -1:
            if not dfs(i, 0):
                return []
    
    return colors

# Input
n = 11
edges = [[6,10],[5,8],[0,4],[0,10],[4,8],[5,9],[8,10],[1,3],[2,5],[4,7],[2,10],[3,6],[7,10],[1,4],[1,10]]

# Get the result
result = can_two_color(n, edges)

print(result)