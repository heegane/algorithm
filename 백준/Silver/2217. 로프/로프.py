import sys

input = sys.stdin.readline

n = int(input())
rope_w = []
for _ in range(n):
    rope_w.append(int(input()))
rope_w.sort()

result = []
for i in range(n):
    result.append(rope_w[i] * n)
    n -= 1
print(max(result))
