import heapq
import sys

n = int(input())
heap = []

for _ in range(n):
    data = sys.stdin.readline().rstrip()
    if data == '0':
        if len(heap) == 0:
            sys.stdout.write("-1\n")
        else:
            sys.stdout.write(str(-heapq.heappop(heap)) + "\n")
    else:
        data = list(map(int, data.split()))
        for _ in range(data[0]):
            heapq.heappush(heap, -data.pop())
