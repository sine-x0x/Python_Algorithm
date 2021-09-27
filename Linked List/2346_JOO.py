import sys
n = int(sys.stdin.readline())

ballon = list(map(int, sys.stdin.readline().split()))
indexl = [i+1 for i in range(n)]
result = []
index = 0
move = ballon.pop(index)
result.append(indexl.pop(index))
while len(ballon)>0:
    if 0<=move:
        index = (index + move-1)%len(ballon)
    else:
        index = (index + move)%len(ballon)
    move = ballon.pop(index)
    result.append(indexl.pop(index))

for j in range(n):
    print(result[j], end=" ")

class ballon(object):
    def __int(self,idx,move,next):
        self.idx = idx
        self.move = move
        self.next = next