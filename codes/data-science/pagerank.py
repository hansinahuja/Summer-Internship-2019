import random

#Function to check if all nodes have been visited
def check_visits(visited, n):
    for i in range(n):
        if visited[i]==0:
            return 0
    return 1

#Simulating a uniform walk
def uniform_walk(graph, n):
    visited = list(0 for i in range(n))
    steps=0
    next_visit =  random.randint(0, n-1)
    visited[next_visit] += 1
    while check_visits(visited,n)!=1:
        next_visit = random.choice(graph[next_visit])
        visited[next_visit] += 1
        steps += 1
    return steps

#Simulating a walk with 2 crawlers
def multiple_crawlers_walk(graph, n):
    visited = list(0 for i in range(n))
    steps=0
    next_visit1 =  random.randint(0, n-1)
    visited[next_visit1] += 1
    next_visit2 =  random.randint(0, n-1)
    visited[next_visit2] += 1
    while check_visits(visited,n)!=1:
        next_visit1 = random.choice(graph[next_visit1])
        visited[next_visit1] += 1
        next_visit2 = random.choice(graph[next_visit2])
        visited[next_visit2] += 1
        steps += 1
    return steps

#Simulating a walk with teleportation probability = 0.3
def teleportation_walk(graph, n):
    visited = list(0 for i in range(n))
    steps=0
    next_visit =  random.randint(0, n-1)
    visited[next_visit] += 1
    while check_visits(visited,n)!=1:
        next_move = random.randint(1,10)
        if next_move<8:
            next_visit = random.choice(graph[next_visit])
        else:
            next_visit =  random.randint(0, n-1)
        visited[next_visit] += 1
        steps += 1
    return steps

#Simulating a non-uniform walk based on degree of nodes
def non_uniform_walk(graph, n, in_degree):
    visited = list(0 for i in range(n))
    steps=0
    next_visit =  0
    visited[next_visit] += 1
    while check_visits(visited,n)!=1:
        prob_next_visit = list()
        for i in range(len(graph[next_visit])):
            node = graph[next_visit][i]
            numerator = 1/in_degree[node]
            prob_next_visit.append(numerator)
        Sum = sum(prob_next_visit)
        for i in range(len(graph[next_visit])):
            prob_next_visit[i] = prob_next_visit[i]/Sum
        for i in range(1, len(graph[next_visit])):
            prob_next_visit[i] += prob_next_visit[i-1]
        next_move = random.uniform(0,1)
        if next_move<prob_next_visit[0]:
            next_visit=graph[next_visit][0]
            visited[next_visit] += 1
            steps += 1
            continue
        for i in range(len(graph[next_visit])):
            if next_move>prob_next_visit[i] and next_move<prob_next_visit[i+1]:
                next_visit = graph[next_visit][i+1]
                break
        visited[next_visit] += 1
        steps += 1
    return steps

#Generating a random graph
n=100
graph = list()
in_degree = list(0 for i in range(n))
for i in range(n):
    row_i = list()
    for j in range(n):
        if i==j:
            continue
        else:
            entry = random.randint(0,1)
            if entry==1:
                row_i.append(j)
                in_degree[j] += 1
    graph.append(row_i)


uniform_walk_steps=0
multiple_crawler_steps=0
teleportation_walk_steps=0
non_uniform_walk_steps=0


for i in range(n):
    uniform_walk_steps += uniform_walk(graph, n)
    multiple_crawler_steps += multiple_crawlers_walk(graph, n)
    teleportation_walk_steps += teleportation_walk(graph, n)
    non_uniform_walk_steps += non_uniform_walk(graph, n, in_degree)

print("Average no. of steps in uniform walk = ", uniform_walk_steps//n)
print("Average no. of steps in 2 crawler walk = ", multiple_crawler_steps//n)
print("Average no. of steps in teleportation walk = ", teleportation_walk_steps//n)
print("Average no. of steps in non-uniform walk = ", non_uniform_walk_steps//n)
