import sys

N, M = map(int, input().split())
data = list(map(int, input().split()))
sum_data = [0] * (N + 1)

for i in range(1, N + 1):
    sum_data[i] = sum_data[i - 1] + data[i - 1]

for _ in range(M):
    first, second = map(int, sys.stdin.readline().rstrip().split())
    result = sum_data[second] - sum_data[first - 1]
    sys.stdout.write(str(result) + "\n")
