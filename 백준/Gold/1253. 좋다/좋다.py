import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
answer = 0

for i in range(n):
    flag = False
    left, right = 0, len(a) - 1
    while left < right:
        if a[left] + a[right] == a[i]:
            # 자기 자신의 수를 쓰면 안됨
            if left == i:
                left += 1
            elif right == i:
                right -= 1
            else:
                flag = True
                break
        elif a[left] + a[right] > a[i]:
            right -= 1
        else:
            left += 1
    # 좋은 수
    if flag:
        answer += 1
print(answer)
