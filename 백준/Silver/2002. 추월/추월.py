import sys

input = sys.stdin.readline

n = int(input())
answer = 0
h = {}
i = 1
result = []
for _ in range(n):
    h[input().rstrip()] = i
    i += 1

for _ in range(n):
    car = input().rstrip()
    result.append((car, h[car]))

for i in range(n - 1):
    if any(result[i][1] > value for key, value in result[i + 1::]):
        answer += 1

print(answer)
