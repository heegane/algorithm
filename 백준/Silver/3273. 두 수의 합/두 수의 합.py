import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())

a.sort()
left, right = 0, n - 1
answer = 0

while left < right:
    if a[left] + a[right] == x:
        answer += 1
        right -= 1
        left += 1
    elif a[left] + a[right] > x:
        right -= 1
    else:
        left += 1

print(answer)
