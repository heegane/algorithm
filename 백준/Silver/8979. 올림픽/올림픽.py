import sys

input = sys.stdin.readline

n, k = map(int, input().split())
li = []

for _ in range(n):
    li.append(list(map(int, input().split())))

li.sort(key=lambda x: (-x[1], -x[2], -x[3]))

answer = 0
for element in li:
    if element[0] == k:
        break
    answer += 1

print(answer)
