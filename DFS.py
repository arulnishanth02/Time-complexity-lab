def dfs(v, visited, graph):
    visited[v] = True
    print(v, end=" ")
    for i in range(len(graph)):
        if graph[v][i] and not visited[i]:
            dfs(i, visited, graph)

n = int(input("Enter number of vertices: "))
graph = []

print("Enter adjacency matrix:")
for _ in range(n):
    graph.append(list(map(int, input().split())))

start = int(input("Enter starting vertex: "))
visited = [False]*n
print("DFS Traversal:")
dfs(start, visited, graph)