import sys

N = int(input())
scores = []

for _ in range(N):
    data = float(sys.stdin.readline().rstrip())
    scores.append(data)

scores.sort()

for i in range(7):
    print("%0.3f" % scores[i])
