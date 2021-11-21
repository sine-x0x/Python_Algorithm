n = int(input())
m = int(input())


graph = {}
for i in range(n):
    graph[i+1] = list()

for i in range(m):
    o,t = map(int,input().split())
    graph[o].append(t)
    graph[t].append(o)


cnt = 0
ff = []
for i in graph[1]:
    ff.append(i)

for i in graph[1]:
    for g in graph[i]:
        if ff.count(g) == 0:
            ff.append(g)

if len(ff)==0:
    print(cnt)
else:
    cnt = len(ff)-1
    print(cnt)