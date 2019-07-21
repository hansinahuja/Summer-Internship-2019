import random
import copy
import math

def coalesce(graph):
    if len(graph)==2:
        return

    u = random.randint(0, len(graph)-1)
    v = random.randint(0, len(graph)-1)
    while graph[u][v]==0:
        u = random.randint(0, len(graph)-1)
        v = random.randint(0, len(graph)-1)
    if v<u:
        u, v = v, u
    row_u = graph[u]
    row_v = graph[v]

    for i in range(len(graph)):
        if i==u or i==v:
            continue
        else:
            new = graph[i][u] + graph[i][v]
            graph[i].pop(v)
            graph[i].pop(u)
            graph[i].append(new)
    graph.pop(v)
    graph.pop(u)
    new_row = []
    for i in range(len(row_u)):
        if i==u or i==v:
            continue
        else:
            new_row.append(row_u[i]+row_v[i])
    new_row.append(0)
    graph.append(new_row)
    coalesce(graph)



n = int(input("Enter number of nodes: "))
print("Enter adjacency matrix row by row: ")
graph = list()
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

global_min_cut = 9999


trials = int((n*(n-1)*math.log(n))/2)
for i in range(trials):
    duplicate = copy.deepcopy(graph)
    coalesce(duplicate)
    if duplicate[0][1] < global_min_cut:
        global_min_cut = duplicate[0][1]

print("Global minimum cut =", global_min_cut)

