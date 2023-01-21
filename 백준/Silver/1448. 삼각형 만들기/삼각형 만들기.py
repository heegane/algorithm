import sys

data = []
N = int(input())
for _ in range(N):
    data.append(int(sys.stdin.readline().rstrip()))

data.sort(reverse=True)

result = 0
for i in range(len(data) - 2):
    if data[i] < data[i + 1] + data[i + 2]:
        result = data[i] + data[i + 1] + data[i + 2]
        print(result)
        exit(0)
    else:
        continue

print(-1)
