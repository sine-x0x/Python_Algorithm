import sys
n = int(sys.stdin.readline())

q=[]

for _ in range(n):
    p = list(sys.stdin.readline().split())
    if len(p)==2:
        q.append(int(p[1]))
    elif p[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))
    elif p[0] == "size":
        print(len(q))
    elif p[0] == "empty":
        print(int(len(q)==0))
    elif p[0] == "front":
        if len(q) ==0:
            print(-1)
        else:
            print(q[0])
    elif p[0] == "back":
        if len(q) ==0:
            print(-1)
        else:
            print(q[-1])

