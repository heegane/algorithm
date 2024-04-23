import sys

input = sys.stdin.readline

n = int(input())
names = []
for _ in range(n):
    names.append(input().rstrip())

increasing = sorted(names)
decreasing = sorted(names, reverse=True)

if names == increasing:
    print("INCREASING")
elif names == decreasing:
    print("DECREASING")
else:
    print("NEITHER")
