from collections import deque

n = int(input("Enter number of vertices: "))
graph = []

print("Enter adjacency matrix:")
for _ in range(n):
    graph.append(list(map(int, input().split())))

start = int(input("Enter starting vertex: "))
visited = [False]*n
queue = deque([start])
visited[start] = True

print("BFS Traversal:")
while queue:
    v = queue.popleft()
    print(v, end=" ")
    for i in range(n):
        if graph[v][i] and not visited[i]:
            queue.append(i)
            visited[i] = True