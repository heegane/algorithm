import sys

N, M = map(int, input().split())
data = {}
count = 0

for _ in range(N):
    data[sys.stdin.readline().rstrip()] = 1
for _ in range(M):
    find = sys.stdin.readline().rstrip()
    if find in data:
        count += 1
    else:
        continue

print(count)
