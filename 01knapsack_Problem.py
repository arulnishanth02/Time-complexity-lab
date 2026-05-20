n = int(input("Enter number of items: "))

values = []
weights = []

print("Enter value and weight of items:")
for _ in range(n):
    v, w = map(int, input().split())
    values.append(v)
    weights.append(w)

W = int(input("Enter knapsack capacity: "))

K = [[0]*(W+1) for _ in range(n+1)]

for i in range(1, n+1):
    for w in range(W+1):
        if weights[i-1] <= w:
            K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]], K[i-1][w])
        else:
            K[i][w] = K[i-1][w]

print("Maximum value =", K[n][W])