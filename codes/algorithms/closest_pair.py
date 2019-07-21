def distance(p1, p2):
    return (((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))**0.5

def closest_pair(points_x, points_y):
    if len(points_x)==2:
        return distance(points_x[0], points_x[1])
    if len(points_x)==3:
        return min(distance(points_x[0], points_x[1]), distance(points_x[1], points_x[2]), distance(points_x[0], points_x[2]))

    mid = len(points_x)//2
    q_x = points_x[0:mid]
    r_x = points_x[mid: ]
    reference = q_x[-1]
    q_y = list()
    r_y = list()
    for i in range(len(points_y)):
        if points_y[i][0]<=reference[0]:
            q_y.append(points_y[i])
        else:
            r_y.append(points_y[i])
    delta = min(closest_pair(q_x, q_y), closest_pair(r_x, r_y))

    region =  list()



    for i in range(len(points_y)):
        if abs(points_y[i][0]-reference[0])<=delta:
            region.append(points_y[i])

    for i in range(len(region)):
        for j in range(i+1, len(region)):
            if abs(region[i][1] - region[j][1]) > 1.5*delta:
                break
            else:
                if distance(region[i], region[j])<delta:
                    delta = distance(region[i], region[j])
    return delta




n = int(input("Enter number of coordinates: "))
points_x = list()
for i in range(n):
    print("For point", i+1, ": ")
    x = int(input("x = "))
    y = int(input("y = "))
    points_x.append((x, y))
points_x.sort()
points_y = points_x
points_y.sort(key = lambda x: x[1])
print(closest_pair(points_x, points_y))

