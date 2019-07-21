# Input section
n = int(input("Enter number of vertices: "))
print()

print("Enter adjacency matrix (input weight of the edge, if it exists, and 0 otherwise):")
graph = list()
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
print()

# Initialization section
vertex = [i for i in range(n)]
key = [999999 for i in range(n)]
parent = [-1 for i in range(n)]

# Prim's algorithm
key[0] = 0
while len(vertex)>0:
    min = 999999
    for i in range(n):
        if (key[i]<min) and (i in vertex):
            min = key[i]
            pick = i
    vertex.remove(pick)
    neighbours = graph[pick]
    for i in range(n):
        if neighbours[i]==0:
            continue
        else:
            if neighbours[i]<key[i] and i in vertex:
                key[i]=neighbours[i]
                parent[i]=pick

# Printing section
print("Minimum spanning tree includes edges:")
for i in range(1, n):
    print(i+1, " - ", parent[i]+1)

weight = 0
for i in range(1, n):
        weight += graph[i][parent[i]]
print("\nWeight of minimum spanning tree =", weight)
