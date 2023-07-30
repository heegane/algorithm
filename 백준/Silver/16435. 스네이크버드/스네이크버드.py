import sys
from collections import deque

n, l = map(int, sys.stdin.readline().rstrip().split())
hs = list(map(int, sys.stdin.readline().rstrip().split()))
hs.sort()
hs = deque(hs)

while True:
    if len(hs) == 0:
        break
    h = hs[0]
    if l < h:
        break
    else:
        l += 1
        hs.popleft()

sys.stdout.write(str(l))
