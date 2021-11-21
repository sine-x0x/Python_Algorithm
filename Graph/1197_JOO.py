v,e = map(int,input().split())

al =[]

am = [[0]*v for i in range(v)]
for i in range(e):
    a,b,w = map(int,input().split())
    am[a-1][b-1] = w
    am[b-1][a-1] = w

print(am)