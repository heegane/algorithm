import heapq
import sys

heap = []

N = int(input())

for _ in range(N):
    data = int(sys.stdin.readline().rstrip())

    if data != 0:
        heapq.heappush(heap, data)
    else:
        if len(heap) == 0:
            sys.stdout.write("0\n")
        else:
            sys.stdout.write(str(heapq.heappop(heap)) + "\n")
