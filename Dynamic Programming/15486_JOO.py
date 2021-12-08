import sys
input = sys.stdin.readline

N = int(input())

days = list()
income = list()

for i in range(N):
    d, p = map(int, input().split())
    days.append(d)
    income.append(p)
income.append(0)
dp = [0 for _ in range(N+1)]


for i in range(N-1,-1,-1):
    if days[i] + i > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], income[i] + dp[i + days[i]])

print(dp[0])