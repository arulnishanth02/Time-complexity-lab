import sys

def tsp(graph, visited, curr, n, count, cost):
    if count == n and graph[curr][0]:
        return cost + graph[curr][0]
    ans = sys.maxsize
    for i in range(n):
        if not visited[i] and graph[curr][i]:
            visited[i] = True
            ans = min(ans, tsp(graph, visited, i, n, count+1, cost+graph[curr][i]))
            visited[i] = False
    return ans

n = int(input("Enter number of cities: "))
graph = []
print("Enter cost matrix:")
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [False]*n
visited[0] = True

print("Minimum travelling cost =", tsp(graph, visited, 0, n, 1, 0))