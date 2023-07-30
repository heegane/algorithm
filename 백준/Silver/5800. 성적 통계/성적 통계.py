import sys
from collections import deque

k = int(sys.stdin.readline())

for i in range(1, k + 1):
    scores = deque(list(map(int, sys.stdin.readline().rstrip().split())))
    n = scores.popleft()
    scores = list(scores)
    scores.sort(reverse=True)
    gap = []

    left = scores[0]
    for j in range(1, n):
        gap.append(left - scores[j])
        left = scores[j]

    sys.stdout.write("Class " + str(i) + "\n")
    sys.stdout.write("Max " + str(max(scores)) + ", Min " + str(min(scores)) + ", Largest gap " + str(max(gap)) + "\n")
