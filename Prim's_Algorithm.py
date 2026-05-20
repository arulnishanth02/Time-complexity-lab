import sys

n = int(input("Enter number of vertices: "))
cost = []

print("Enter adjacency matrix:")
for i in range(n):
    cost.append(list(map(int, input().split())))

visited = [False]*n
visited[0] = True
edges = 0
mincost = 0

while edges < n-1:
    minimum = sys.maxsize
    a = b = -1
    for i in range(n):
        if visited[i]:
            for j in range(n):
                if not visited[j] and cost[i][j] != 0:
                    if cost[i][j] < minimum:
                        minimum = cost[i][j]
                        a, b = i, j
    print("Edge:", a, "-", b, "Cost:", minimum)
    mincost += minimum
    visited[b] = True
    edges += 1

print("Minimum Cost =", mincost)