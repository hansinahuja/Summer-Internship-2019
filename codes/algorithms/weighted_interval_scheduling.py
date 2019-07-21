# Function to fill the dynamic programming array
def max_weight(tasks, p, n, dp):
    if n==0:
        return 0
    if dp[n-1] != -1:
        return dp[n-1]
    else:
        dp[n-1] = max(max_weight(tasks, p, n-1, dp), tasks[n-1][2]+max_weight(tasks, p, p[n-1], dp))
        return dp[n-1]

# Function to print tasks to be performed
def print_tasks(tasks, p, n, dp):
    if n==0:
        return
    else:
        if tasks[n-1][2]+dp[n-1] >= dp[n-2]:
            print("Task", n-1)
            print_tasks(tasks, p, p[n-1], dp)
        else:
            print_tasks(tasks, p, n-1, dp)


# Input section
n = int(input("Enter number of tasks: "))

tasks = list()
p = list()
dp = list(-1 for i in range(n))

for i in range(n):
    s = int(input("Enter start time for " + str(i+1) + "th task: "))
    e = int(input("Enter end time for " + str(i+1) + "th task: "))
    w = int(input("Enter weight for " + str(i+1) + "th task: "))
    tasks.append((e, s, w))

# Running the algorithm
tasks.sort()

for i in range(len(tasks)):
    j=i-1
    flag=0
    while(j>=0):
        if tasks[j][0]<=tasks[i][1]:
            p.append(j+1)
            flag=1
            break
        j=j-1
    if flag==0:
        p.append(0)

# Printing section
print("\nMaximum weight possible =", max_weight(tasks, p, n, dp))
print("The tasks performed must be:")
print_tasks(tasks, p, n, dp)
