import sys

input = sys.stdin.readline

n, m = map(int, input().split())
li = []
if n == 1:
    li = [int(input())]
else:
    li = list(map(int, input().split()))

if m == 1:
    li += [int(input())]
else:
    li += list(map(int, input().split()))

li.sort()
print(*li)
