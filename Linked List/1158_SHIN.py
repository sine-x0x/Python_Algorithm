import sys
n,k = map(int,sys.stdin.readline().split())

cir = [i+1 for i in range(n)]

cir_loc=k-1
res=[]

while len(cir): # while 0 false, while Z true
    if cir_loc >= len(cir):
        cir_loc-=len(cir)
    else:
        res.append(str(cir.pop(cir_loc)))
        cir_loc+=k-1

print('<',', '.join(res),'>',sep='')