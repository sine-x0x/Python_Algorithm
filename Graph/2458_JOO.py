import sys
input = sys.stdin.readline

N,M = map(int,input().split())

height = [[0 for _ in range(N+1)] for _ in range(N+1)]
tall = [set() for _ in range(N+1)]
short = [set() for _ in range(N+1)] ## use set incase of duplicates during update


for _ in range(M):
    a,b = map(int, input().split())
    tall[a].add(b)
    short[b].add(a)

for i in range(1,N+1):
    for j in short[i]:
        tall[j].update(tall[i]) ## those taller than i are taller than j
    for j in tall[i]:
        short[j].update(short[i])

cnt = 0
for i in range(1,N+1):
    if len(tall[i])+len(short[i])==N-1:
        cnt += 1

print(cnt)