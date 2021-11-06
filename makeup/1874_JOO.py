import sys

input = sys.stdin.readline

n = int(input())

stk = []
ans = []
count = 1
poss = True


for i in range(n):
    num = int(input())
    while count <= num:
        stk.append(count)
        ans.append('+')
        count+=1
    if stk[-1] == num:
        stk.pop()
        ans.append('-')
    else:
        poss = False

if poss == False:
    print("NO")
else:
    for i in ans:
        print(i)
