n = int(input("Enter number of tasks: "))

l = list()

for i in range(n):
    s = int(input("Enter start time for " + str(i) + "th task: "))
    e = int(input("Enter end time for " + str(i) + "th task: "))
    l.append((e, s))

l.sort()

last_end = 0
# print(l[1][0])
for i in range(n):
    if last_end <= l[i][1]:
        print(l[i][1], l[i][0])
        last_end = l[i][0]
