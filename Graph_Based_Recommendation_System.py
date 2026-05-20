from collections import defaultdict

n_users = int(input("Enter number of users: "))
n_items = int(input("Enter number of items: "))

adj = defaultdict(set)
print("Enter user-item interactions (user item):")
for _ in range(int(input("Enter number of interactions: "))):
    u, i = map(int, input().split())
    adj[u].add(i)

user = int(input("Enter user for recommendation: "))
recommended = set()
for u, items in adj.items():
    if u != user:
        recommended.update(items - adj[user])

print("Recommended items for user", user, ":", recommended)