import heapq
import sys

heap = [0] * 100001

N = int(input())

for _ in range(N):
    data = int(sys.stdin.readline().rstrip())
    if data != 0:
        heapq.heappush(heap, -data)
    else:
        sys.stdout.write(str(-heapq.heappop(heap)) + "\n")
