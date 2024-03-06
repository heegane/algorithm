n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
left, right = 0, 1

while right <= n and left <= right:
    total = sum(arr[left:right])

    if total == m:
        answer += 1
        left += 1
        right += 1

    elif total < m:
        right += 1

    else:
        left += 1

print(answer)
