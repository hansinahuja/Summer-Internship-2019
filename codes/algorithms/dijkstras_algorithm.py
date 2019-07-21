# Input section
n = int(input("Enter number of vertices: "))
print()

print("Enter adjacency matrix (input weight of the edge, if it exists, and 0 otherwise):")
graph = list()
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
print()

s = int(input("Enter starting node: "))
d = int(input("Enter destination node: "))
s = s-1
d = d-1
print()

# Initialization section
not_visited = [i for i in range(n)]
min_distances = [999999 for i in range(n)]
min_distances[s] = 0

# Dijkstra's algorithm
while d in not_visited:
    min = 999999
    target_node = None

    for node in not_visited:
        if min_distances[node]<min:
            min = min_distances[node]
            target_node = node

    not_visited.remove(target_node)

    neighbour_distances = graph[target_node]

    for i in range(n):
        if neighbour_distances[i]==0:
            continue
        else:
            if min_distances[i] > min_distances[target_node] + neighbour_distances[i]:
                min_distances[i] = min_distances[target_node] + neighbour_distances[i]

#Printing the answer
print("Sum of weights of shortest path =", min_distances[d])
