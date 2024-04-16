import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = []
# 두 수의 차 저장
result = []

for _ in range(n):
    a.append(int(input()))

a.sort(reverse=True)
left, right = 0, 0

while left <= right and 0 <= left < n and 0 <= right < n:
    v = a[left] - a[right]
    if v >= m:
        result.append(v)
        left += 1
    else:
        right += 1

print(min(result))
