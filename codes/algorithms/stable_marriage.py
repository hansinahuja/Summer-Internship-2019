import random

n = int(input("Enter number of suitors of each gender: "))

pref_order_men = list()
pref_order_women = list()
current_state_men = list()
current_state_women = list()
free_men = list()

for i in range(n):
    temp = list(map(int,input("Enter preference list for " + str(i) + "th man: ").split()))
    pref_order_men.append(temp)
    current_state_men.append(temp)
    free_men.append(i)

for i in range(n):
    temp = list(map(int,input("Enter preference list for " + str(i) + "th woman: ").split()))
    pref_order_women.append(temp)
    current_state_women.append(-1)

while len(free_men) != 0:
    rand = random.randint(0, len(free_men)-1)
    proposer = free_men[rand]
    proposal = current_state_men[proposer][0]
    fiancee = current_state_women[proposal]
    current_state_men[proposer].remove(proposal)
    if fiancee==-1:
        current_state_women[proposal] = proposer
        free_men.remove(proposer)
        continue
    proposer_priority = pref_order_women[proposal].index(proposer)
    fiancee_priority = pref_order_women[proposal].index(fiancee)
    if proposer_priority < fiancee_priority:
        current_state_women[proposal] = proposer
        free_men.remove(proposer)
        free_men.append(fiancee)


for i in range(n):
    print(current_state_women[i], i)
