import random
import matplotlib.pyplot as plt

n=100                       #number of tosses goes from 1 to n
repeat_experiment = 10000    #repeat each experiment 100 times
longest_streaks = list()

for coins in range(1, n+1):
    longest_streaks_for_coins = list()
    for i in range(repeat_experiment):
        previous_toss = random.randint(0, 1)
        current_streak = 1
        max_streak = 1
        for j in range(1, coins):
            next_toss = random.randint(0, 1)
            if next_toss==previous_toss:
                current_streak += 1
            else:
                current_streak=1
                previous_toss=next_toss
            if max_streak<current_streak:
                max_streak=current_streak
        longest_streaks_for_coins.append(max_streak)
    longest_streaks.append(sum(longest_streaks_for_coins)/repeat_experiment)

number_of_tosses = list(i for i in range(1, n+1))

plt.plot(number_of_tosses, longest_streaks)
plt.show()
