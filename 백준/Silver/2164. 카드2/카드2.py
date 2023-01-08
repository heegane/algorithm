import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()

for i in range(1, N + 1):
    queue.append(i)

for i in range(N - 1):
    queue.popleft()
    pop_value = queue.popleft()
    queue.append(pop_value)

print(queue[0])