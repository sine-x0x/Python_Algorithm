v, e, s = map(int,input().split())

graph = {}
for i in range(v):
    graph[i+1] = list()

for i in range(e):
    o,t = map(int,input().split())
    graph[o].append(t)
    graph[t].append(o)

for i in range(v):
    if len(graph[i+1])!=0:
        graph[i+1].sort()


def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            print(node, end=" ")
            visit.append(node)
            ordered = graph[node]
            for i in range(len(ordered)):
                stack.append(ordered[-(i+1)]) ## visit smaller node first

    return visit

def bfs(graph, start_node):
    visit = list()
    queue = list()
    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            print(node, end=" ")
            visit.append(node)
            queue.extend(graph[node])

    return visit


dfs(graph,s)
print()
bfs(graph,s)

