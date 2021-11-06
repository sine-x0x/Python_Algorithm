import sys

input = sys.stdin.readline

n = int(input())
a = list()

for _ in range(n):
    a.append(float(input()))

a.sort()


for i in range(7):
    b = "{:.3f}".format(a[i])
    print(b)