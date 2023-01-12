import sys
from collections import Counter

N = int(input())
nums = list()

for _ in range(N):
    data = int(sys.stdin.readline().rstrip())
    nums.append(data)

nums.sort()

if len(nums) == 1:
    mid = nums[0]
    cnt = Counter(nums).most_common(1)
    result_mode = cnt[0][0]
else:
    mid_index = N // 2
    mid = nums[mid_index]
    cnt = Counter(nums).most_common(2)
    if cnt[0][1] == cnt[1][1]:
        result_mode = cnt[1][0]
    else:
        result_mode = cnt[0][0]

print(round(sum(nums) / N))
print(mid)
print(result_mode)
print(max(nums) - min(nums))
