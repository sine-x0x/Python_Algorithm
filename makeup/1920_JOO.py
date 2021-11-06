import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
dix = {}
for i in a:
    dix[i] =1

m = int(input())
b = list(map(int,input().split()))

for i in b:
    if i in dix:
        print("1")
    else:
        print("0")

### or also able with binary search