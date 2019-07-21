# Input section
n = int(input("Enter number of vertices: "))
print()

print("Enter adjacency matrix:")
graph = list()
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
print()

# Breadth first search
queue = []
visited = [0 for i in range(n)]
queue.append(0)
visited[0] = 1
print("Breadth first traversal starting from node 1:")
while len(queue)!=0:
    neighbours = graph[queue[0]]
    print(queue[0]+1, end=" ")
    del queue[0]
    for i in range(n):
        if neighbours[i]==1 and visited[i]==0:
            queue.append(i)
            visited[i]=1
