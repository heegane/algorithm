import sys

input = sys.stdin.readline

n = int(input())
li = sorted(list(map(int, input().split())))

left, right = 0, n - 1
answer_a, answer_b = 0, 0
cmp_v = 2000000000

while left < right:
    sum_v = li[left] + li[right]

    if abs(sum_v) < cmp_v:
        cmp_v = abs(sum_v)
        answer_a, answer_b = li[left], li[right]
        if sum_v == 0:
            break

    # 0에 가깝게 하기 위해
    # 음수일 때
    if sum_v < 0:
        left += 1
    # 양수일 때
    else:
        right -= 1

print(answer_a, answer_b)
