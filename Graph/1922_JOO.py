import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = 999

visited = [False] * N
distances = [INF] * N
adj_mat = [[INF]*N for _ in range(N)]

for _ in range(M):
    s,d,w = map(int,input().split())
    adj_mat[s-1][d-1] = w
    adj_mat[d-1][s-1] = w

def get_min_node(node_num):
    for i in range(node_num):
        if not visited[i]:
            v = i
            break
    for i in range(node_num):
        if not visited[i] and distances[i] < distances[v]:
            v = i

    return v


def prim(start, node_num):
    # distances 배열과 visted 배열 초기화
    for i in range(node_num):
        visited[i] = False
        distances[i] = INF

    # 시작노드의 distance 값을 0으로 초기화
    distances[start] = 0
    for i in range(node_num):
        node = get_min_node(node_num)
        visited[node] = True    # node 를 방문했다 표시

        for j in range(node_num):
            if adj_mat[node][j] != INF:
                if not visited[j] and adj_mat[node][j] < distances[j]:
                    distances[j] = adj_mat[node][j]


prim(0,N)
print(distances)
print(sum(distances))





