import random
import matplotlib.pyplot as plt

number_of_people = 10000
trials = 10000
sum_of_guesses = list()

for j in range(trials):
    sum = 0
    for i in range(number_of_people):
        sum += random.randint(1, 100)
    sum_of_guesses.append(sum)

plt.hist(sum_of_guesses, bins=100)
plt.show()
