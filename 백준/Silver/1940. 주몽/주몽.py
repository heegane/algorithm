import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
nums = list(map(int, input().split()))
nums.sort()

left, right = 0, len(nums) - 1
answer = 0

while left < right:

    total = nums[left] + nums[right]

    if total == m:
        answer += 1
        left += 1
        right -= 1

    elif total < m:
        left += 1

    else:
        right -= 1

print(answer)
