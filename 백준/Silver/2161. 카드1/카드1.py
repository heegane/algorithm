import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()
discard = deque()

for i in range(1, N + 1):
    queue.append(i)

for i in range(N - 1):
    discard.append(queue.popleft())
    pop_value = queue.popleft()
    queue.append(pop_value)

discard.append(queue.popleft())

for _ in range(N):
    result_value = discard.popleft()
    print(f"{result_value}", end=" ")
