import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())
a = []
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        if a:
            print(-heapq.heappop(a))
        else:
            print(0)
    else:
        heapq.heappush(a, -x)
