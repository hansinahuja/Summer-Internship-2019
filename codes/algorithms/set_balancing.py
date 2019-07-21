import random
A = []
b = []
c = []
abs_c = []
n = int(input("Enter n: "))

for i in range(n):
    b.append(random.randint(0, 1))
    if b[i]==0:
        b[i]=-1

for i in range(n):
    row = []
    result = 0
    for j in range(n):
        row.append(random.randint(0, 1))
        result += (row[j]*b[j])
    A.append(row)
    c.append(result)
    abs_c.append(abs(result))

print("Maximum imbalance for generated matrix =", max(abs_c))
