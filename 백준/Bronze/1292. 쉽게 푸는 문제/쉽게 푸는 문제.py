import sys

input = sys.stdin.readline

a, b = map(int, input().split())
li = []

for i in range(1, b + 1):
    for j in range(i):
        li.append(i)

print(sum(li[a - 1:b]))
