# Function to find minimum edge
def findMinimum(graph, n):
    min = 9999999
    for i in range(n):
        for j in range(n):
            if graph[i][j]<min and graph[i][j]>0:
                min=graph[i][j]
                v1 = i
                v2 = j
    graph[v1][v2] = 0
    graph[v2][v1] = 0
    return v1, v2, min

# Input section
n = int(input("Enter number of vertices: "))
print()

print("Enter adjacency matrix (input weight of the edge, if it exists, and 0 otherwise):")
graph = list()
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
print()

# Kruskal's algorithm
vertices = []
edges = []
weight = 0
while len(edges)!=(n-1):
    i, j, w = findMinimum(graph, n)
    if (i in vertices) and (j in vertices):
        continue
    else:
        weight += w
        edges.append([i, j])
        if i in vertices:
            vertices.append(j)
        else:
            vertices.append(i)

# Printing section
print("Minimum spanning tree includes edges:")
for edge in edges:
    print(edge[0]+1, " - ", edge[1]+1)
print("\nWeight of minimum spanning tree =", weight)
