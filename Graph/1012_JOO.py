num = int(input())

binggle = [[1,0],[0,1],[-1,0],[0,-1]]

def search(x, y):
    filled = [[x, y]]
    while filled:
        curr = filled.pop(0)
        for i in range(4):
            q = curr[0] + binggle[i][0]
            w = curr[1] + binggle[i][1]
            if  0 <= q < n and 0 <= w < m and batt[q][w] == 1:
                batt[q][w] = 0
                filled.append([q, w])


for i in range(num):
    m,n,k = map(int,input().split())
    batt = [[0] * m for i in range(n)]
    cnt = 0
    for _ in range(k):
        y,x = map(int,input().split())
        batt[x][y] = 1
    for j in range(n):
        for k in range(m):
            if batt[j][k] ==1:
                search(j,k)
                batt[j][k] =0
                cnt +=1
    print(cnt)
