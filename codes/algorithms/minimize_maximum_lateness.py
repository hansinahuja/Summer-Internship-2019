n = int(input("Enter number of tasks: "))
tasks = list()
finish_times = list()
current = 0
maximum_lateness = 0

for i in range(n):
    t = int(input("Enter time taken for " + str(i+1) + "th task: "))
    d = int(input("Enter deadline for " + str(i+1) + "th task: "))
    tasks.append((d, t, i+1))

tasks.sort()
print("Tasks must be scheduled in order: ")

for i in range(n):
    print("Task", tasks[i][2])
    finish_times.append(current + tasks[i][1])
    current += tasks[i][1]
    if finish_times[i]>tasks[i][0]:
        if finish_times[i]-tasks[i][0]>maximum_lateness:
            maximum_lateness = finish_times[i]-tasks[i][0]

print("Maximum lateness =", maximum_lateness)
