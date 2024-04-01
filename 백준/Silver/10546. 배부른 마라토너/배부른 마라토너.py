import sys

input = sys.stdin.readline

n = int(input())
h = {}
for _ in range(n):
    name = input().rstrip()
    if name in h:
        h[name] += 1
    else:
        h[name] = 1

for _ in range(n - 1):
    name = input().rstrip()
    if name in h:
        h[name] -= 1

result = list(h.items())
for row in result:
    if row[1] > 0:
        print(row[0])
        break
