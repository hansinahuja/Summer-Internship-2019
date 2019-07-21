a = [-20,-20,0, 20,20,1, 40,40,0, -200,0,0]
n=4

def score(m, c):
    red1=0
    red2=0
    blue1=0
    blue2=0
    for i in range(n):
        val = a[(3*i)+1] - (m*a[3*i]) - c
        if val>0:
            if a[(3*i)+2]==0:
                red1+=1
            else:
                blue1+=1

        if val<0:
            if a[(3*i)+2]==0:
                red2+=1
            else:
                blue2+=1

        if val==0:
            return 999

    min1 = red1+blue2
    min2 = red2+blue1
    if(min1>min2):
        return min2
    else:
        return min1



m=0
c=0
min=999

for m1 in range(-999,999):
    for c1 in range(-999, 999):
        if min>score(m1, c1):
             min=score(m1, c1)
             m=m1
             c=c1

print(m, c)
# for i in range(11):
#     print(a[i])


