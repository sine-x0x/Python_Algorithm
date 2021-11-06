import sys
import heapq

k,n = map(int,sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
gogo = []

for i in a:
    heapq.heappush(gogo,i)


for i in range(n):
    num = heapq.heappop(gogo)
    for j in range(k):
        mul = num*a[j]
        heapq.heappush(gogo,mul)

        if num % a[j] ==0: ### 중복 제거 신기
            break

print(num)