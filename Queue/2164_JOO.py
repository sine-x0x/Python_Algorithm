n = int(input())

a = [x+1 for x in range(n)]


for _ in range(n-1):
    a.pop(0)
    b = a[1:-1] + a[0]
    a = b



print(a[0])