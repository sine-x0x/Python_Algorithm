n,d = map(int, input().split())

road = []

for i in range(n):
    s,e,w = map(int, input().split())
    if e <= d:
        road.append([s, e, w])

position = [i for i in range(d+1)]

for j in range(d+1):
    if j != 0:
        position[j] = min(position[j] , position[j-1]+1) ## two choices ( dijkstra )
    for i in road:
        if i[0] == j:
            position[i[1]] = min(position[i[1]], position[i[0]]+i[2])

print(position[d])

