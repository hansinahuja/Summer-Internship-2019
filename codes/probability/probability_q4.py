import random
import matplotlib.pyplot as plt

number_of_objects = 1000
probability = 0.7
trials = 10000
average_errors = list(0 for i in range(0,100))

for k in range(trials):
    objects = list()
    errors = list()
    sum_of_objects = 0

    for i in range(number_of_objects):
        if(random.uniform(0,1)<probability):
            objects.append(0)
        else:
            objects.append(1)
            sum_of_objects+=1

    true_fraction = sum_of_objects/number_of_objects
    next_batch = 10
    picked=0
    sum=0

    for i in range(100):
        for j in range(next_batch):
            sum += objects[picked]
            picked += 1
        errors.append((abs(true_fraction - (sum/picked))/true_fraction)*100)

    for i in range(0, 100):
        average_errors[i] += errors[i]


for i in range(0, 100):
    average_errors[i] = average_errors[i]/trials

sampling_percentage = list(i for i in range(1, 101))
plt.plot(sampling_percentage, average_errors)
plt.show()

