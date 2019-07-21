import random

#Function to calculate maximum imbalance using randomized approach
def randomized(A):
    b=[]
    for i in range(len(A[0])):
        t=random.randint(0,1)
        if(t==0):
            b.append(-1)
        else:
            b.append(1)
    c=[]
    for row in A:
        val=0
        for j in range(len(b)):
            val += row[j]*b[j]
        c.append(val)
    max=0
    for check in c:
        if abs(check)>max:
            max=abs(check)
    return max

#Function to calculate maximum imbalance using randomized approach
def brute_force(temp, n, A, imbalances):
    b =[]
    for i in range(n):
        if i in temp:
            b.append(1)
        else:
            b.append(-1)
    c = []
    for row in A:
        val = 0
        for j in range(len(b)):
            val += row[j]*b[j]
        c.append(val)
    max = 0
    for check in c:
        if abs(check)>max:
            max=abs(check)
    imbalances.append(max)

#Function to generate the vector b in each iteration
def store_comb(a, n, k, i, temp, A, imbalances):
    if i==k:
        valid = 1
        for h in range(1, k):
            if temp[h]>temp[h-1]:
                continue
            else:
                valid = 0
                break
        if(valid):
            brute_force(temp, n, A, imbalances)
        return
    if i==0:
        min=1
    else:
        min=a[i-1]+1
    for j in range(min, n+1):
        temp.append(j)
        store_comb(a, n, k, i+1, temp, A, imbalances)
        temp.remove(temp[-1])

n=12    #number of people
m=5     #number of features
a=[i for i in range(1, n+1)]
temp=[]
imbalances=[]

A = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(random.randint(0, 1))
    A.append(row)

store_comb(a, n, n//2, 0, temp, A, imbalances)
print("Maximum imbalance using brute force approach =", max(imbalances))
print("Maximum imbalance using randomized approach =", randomized(A))
