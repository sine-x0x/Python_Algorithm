# n = int(input()) #num
# p = []  #price
# min = 3000

# for i in range(n):
#     r,g,b = map(int, input().split())
#     r0 = [r,0]
#     g0 = [g,1]
#     b0 = [b,2]
#     k= [r0,g0,b0]
#     p.append(k)
#
# for i in range(n):
#     p[i].sort()
#
# for i in range()

n = int(input()) #num

p = []
for _ in range(n):
    p.append(list(map(int,input().split())))
# result =[]
# def price(i, prev, value): # i번째 집, prev에 고른 색
#     if i>=n:
#         result.append(value)
#         return
#     else:
#         rgb = [0, 1, 2]
#         rgb.remove(prev)
#         for j in rgb:
#             now = i
#             now_value = value
#             now_value += p[now][j]
#             price(i+1, j, now_value)
#
# price(1,0,p[0][0])
# price(1,1,p[0][1])
# price(1,2,p[0][2])
#
# print(min(result))

for i in range(1,n):
    p[i][0] = min(p[i - 1][1], p[i-1][2]) + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
print(min(p[n-1]))