import random

key=["Adarsh(0)","Atul(1)","Daksh(2)","Diksha(3)","Garima(4)","Gazal(5)","Hansin(6)","Navtej(7)","Pradyumn(8)","Sakshay(9)","Shobhit(10)"]
votes=[0 for i in range(11)]
choices=[[8,6,7],[0,10],[6,8,9],[4,1,9,5],[1,5],[6,9,4],[2, 9],[2,9,10,0,1],[6,4,3,2,7,9],[2, 6],[6,8,5]]
n=100000

start = random.randint(0, 10)
for i in range(n):

    vote_index = random.randint(0, len(choices[start])-1)
    elect = choices[start][vote_index]
    votes[elect] += 1
    start = elect

print("Distriution is \t:\t")
for i in range(11):
    print(key[i], " \t:\t ", votes[i]/n)
print("\nBR elected is \t:\t", key[votes.index(max(votes))])
