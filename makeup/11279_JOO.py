import sys
import heapq # python only supports min heap
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    comm = int(input())
    if comm != 0:
        heapq.heappush(heap, -comm) # we need a max heap but only min --> - the input
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))