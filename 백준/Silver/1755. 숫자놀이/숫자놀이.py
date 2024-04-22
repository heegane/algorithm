import sys

input = sys.stdin.readline

m, n = map(int, input().split())
li = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
nums = [i for i in range(m, n + 1)]
answer = []

for num in nums:
    if num >= 10:
        s = li[num // 10] + " " + li[num % 10]
    else:
        s = li[num]
    answer.append((s, num))

answer.sort(key=lambda x: x[0])

for i in range(len(answer)):
    if i % 10 == 0 and i != 0:
        print()

    print(answer[i][1], end=" ")
