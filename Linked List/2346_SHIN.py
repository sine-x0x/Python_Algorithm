n = int(input())
dou = list(map(int, input().split()))
idx = 0
res = []

index = [i+1 for i in range(n)]
res=[]

dou_loc = dou.pop(idx)
res.append(index.pop(idx))

while dou:
    if dou_loc < 0:
        idx = (idx + dou_loc) % len(dou)
    else:
        idx = (idx + (dou_loc - 1)) % len(dou)
    dou_loc = dou.pop(idx)
    res.append(index.pop(idx))

for r in res:
    print(r, end=' ')

#print(' '.join(res)) 안되는 이유?
