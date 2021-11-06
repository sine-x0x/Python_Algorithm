from collections import deque

n = int(input())

# a = [x+1 for x in range(n)
a = deque([x+1 for x in range(n)])


for i in range(n-1):
    a.popleft()
    b = a.popleft()
    a.append(b)



print(a[0])