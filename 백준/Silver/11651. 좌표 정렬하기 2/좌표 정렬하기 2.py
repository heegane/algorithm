import sys

N = int(input())
result = []

for _ in range(N):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    result.append(data)

result.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(f"{result[i][0]} {result[i][1]}")
