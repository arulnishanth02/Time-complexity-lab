n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []
print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    edges.append((u, v))

vertex_cover = set()

while edges:
    u, v = edges[0]
    vertex_cover.add(u)
    vertex_cover.add(v)
    edges = [edge for edge in edges if u not in edge and v not in edge]

print("Vertex Cover set:", vertex_cover)