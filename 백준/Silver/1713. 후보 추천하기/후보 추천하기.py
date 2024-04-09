import sys

input = sys.stdin.readline

n = int(input())
cnt = int(input())
h = {}
result = []
nums = list(map(int, input().split()))

for num in nums:
    if len(result) < n:
        if num in h:
            h[num] += 1
        else:
            h[num] = 1
            result.append(num)
    else:
        if num in h:
            h[num] += 1
        else:
            li = list(h.items())
            li = sorted(li, key=lambda x: x[1])
            del h[li[0][0]]
            result[result.index(li[0][0])] = num
            h[num] = 1

result.sort()
print(' '.join(map(str, result)))
