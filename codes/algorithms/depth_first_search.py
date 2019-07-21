# Input section
n = int(input("Enter number of vertices: "))
print()

print("Enter graph in edge list format (Enter \"-1 -1\" to exit):")
graph = [[] for i in range(n)]
edges = []
edge = list(map(int, input().split()))
while edge[0]!=-1:
    edge[0] -= 1
    edge[1] -= 1
    edges.append(edge)
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
    edge = list(map(int, input().split()))
print()


# Depth first traversal
stack = []
stack.append(0)
visited = [0 for i in range(n)]
visited[0] = 1
print("Breadth first traversal starting from node 1:")
print(stack[-1]+1, end=" ")
while len(stack)>0:
    flag=0
    for node in graph[stack[-1]]:
        if visited[node]==1:
            continue
        else:
            stack.append(node)
            visited[node]=1
            print(stack[-1]+1, end=" ")
            flag=1
            break
    if flag==0:
        del stack[-1]
