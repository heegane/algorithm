import sys

N = int(input())
scores = []
for _ in range(N):
    data = sys.stdin.readline().split()
    scores.append([data[0], int(data[1]), int(data[2]), int(data[3])])

scores.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(scores[i][0])
