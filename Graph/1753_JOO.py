import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline ## time out

V, E = map(int, input().split())
st = int(input())

graph = defaultdict(list) ### very good
INF = 100000000000000000
distance = [INF] * (V+1)

for _ in range(E):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(queue, (cost, node[0]))


dijkstra(st)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

