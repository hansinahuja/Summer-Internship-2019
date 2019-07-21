import random
import matplotlib.pyplot as plt

n = 1000000
trials = 100
number_of_heads = list()

for i in range(trials):
    heads = 0
    for j in range(n):
        if(random.randint(0, 1) == 1):
            heads+=1
    number_of_heads.append(heads)

    print(i)

experiment = list(i for i in range(1, trials+1))

plt.hist(number_of_heads, bins=10)
plt.show()

