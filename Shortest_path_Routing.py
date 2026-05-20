import sys

n = int(input("Enter number of nodes: "))
graph = []

print("Enter cost matrix:")
for _ in range(n):
    graph.append(list(map(int, input().split())))

source = int(input("Enter source node: "))
dist = [sys.maxsize]*n
visited = [False]*n
dist[source] = 0

for _ in range(n):
    u = -1
    min_dist = sys.maxsize
    for i in range(n):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            u = i
    visited[u] = True
    for v in range(n):
        if graph[u][v] and not visited[v]:
            if dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

print("Shortest distances from node", source, ":")
for i in range(n):
    print("Node", i, "Distance", dist[i])7