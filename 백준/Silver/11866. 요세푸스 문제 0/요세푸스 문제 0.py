import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

queue = deque()
order_queue = deque()

for i in range(1, N + 1):
    queue.append(i)

for _ in range(0, N):
    for _ in range(0, K - 1):
        queue.append(queue.popleft())
    order_queue.append(queue.popleft())

sys.stdout.write("<")
for _ in range(0, N):
    if len(order_queue) == 1:
        sys.stdout.write(str(order_queue.popleft()))
    else:
        sys.stdout.write(str(order_queue.popleft()) + ", ")
sys.stdout.write(">")