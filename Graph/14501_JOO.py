n = int(input())

cases = []
result = []

for _ in range(n):
    c = list(map(int,input().split()))
    cases.append(c)
    result.append(c[1])
result.append(0)

for i in range(n - 1, -1, -1):
    if cases[i][0] + i > n:
        result[i] = result[i + 1]
    else:
        result[i] = max(result[i + 1], cases[i][1] + result[i + cases[i][0]])

print(result[0])

