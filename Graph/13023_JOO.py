n, m = map(int, input().split())


graph = {}
for i in range(n):
    graph[i] = list()

for i in range(m):
    o,t = map(int,input().split())
    graph[o].append(t)
    graph[t].append(o)

visited = [False] * n
# def dfs(graph):
#     for i in range(n):
#         visit = list()
#         stack = list()
#         stack.append(i)
#         while stack:
#             if (len(visit)==4):
#                 return 1
#             node = stack.pop()
#             if node not in visit:
#                 visit.append(node)
#                 stack.extend(graph[node])  ## visit smaller node first
#     return 0
## problem occurs because revisting is allowed

def dfs(idx, number):
    if number == 4:
        print(1)
        exit()
    for i in graph[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, number + 1)
            visited[i] = False

for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)