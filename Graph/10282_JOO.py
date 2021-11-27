import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    dp[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if dp[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if cost < dp[node[0]]:
                dp[node[0]] = cost
                heapq.heappush(queue, (cost, node[0]))

num = int(input())

for _ in range(num):
    n,d,c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    dp = [INF]*(n+1)

    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append([a, s])
    dijkstra(c)

    cnt = 0
    ans = 0
    for i in dp:
        if i != INF:
            cnt += 1
            ans = max(ans, i)

    print(f"{cnt} {ans}")