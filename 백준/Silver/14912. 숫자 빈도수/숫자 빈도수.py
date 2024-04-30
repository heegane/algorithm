import sys

input = sys.stdin.readline

n, d = map(int, input().split())
nums = [i for i in range(1, n + 1)]
answer = 0

for num in nums:
    if len(str(num)) > 1:
        for i in range(len(str(num))):
            if str(num)[i] == str(d):
                answer += 1
    else:
        if str(num) == str(d):
            answer += 1

print(answer)
