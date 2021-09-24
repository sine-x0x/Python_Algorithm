import sys
n,j = map (int,sys.stdin.readline().split())
a = [x+1 for x in range(n)]

result = []
index = j-1

while len(result) != n:
    k = len(a)# 남아있는 숫자 길이
    if index >= k:
        index = index - k
    else:
        result.append(str(a.pop(index)))
        index += (j-1)
print("<",end="")
print( ", ".join(result), end="")
print(">")




