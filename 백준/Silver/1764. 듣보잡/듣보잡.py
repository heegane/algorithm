import sys

N, M = map(int, input().split())
result = []
data = {}

for _ in range(N):
    data[sys.stdin.readline().rstrip()] = 1
for _ in range(M):
    input_data = sys.stdin.readline().rstrip()
    if input_data in data:
        result.append(input_data)
    else:
        continue

result.sort()
sys.stdout.write(str(len(result)) + "\n")
for i in range(len(result)):
    sys.stdout.write(result[i] + "\n")
