import sys

input = sys.stdin.readline

n = int(input())
li = sorted(map(int, input().split()))
left, right = 0, n - 1
answer = li[left] + li[right]

while left < right:
    cmp_v = li[left] + li[right]

    if abs(answer) > abs(cmp_v):
        answer = cmp_v

    if cmp_v < 0:
        left += 1
    else:
        right -= 1

print(answer)
