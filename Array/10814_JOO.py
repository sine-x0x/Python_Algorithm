###### 버블 시도 했는데 시간초과
import sys
n = int(sys.stdin.readline())
l =[]

for _ in range(n):
    l.append(list(sys.stdin.readline().split()))


l.sort(key= lambda e: int(e[0])) #stable sort vs unstable ->> given method merge sort
for i in range(n):
    print(l[i][0],l[i][1])

# p = len(l)-1

# for i in range(n):
#     while p!=0:
#         for j in range(p):
#             if l[j][0] > l[j+1][0]:
#                 l[j],l[j+1] = l[j+1],l[j]
#         p-=1



