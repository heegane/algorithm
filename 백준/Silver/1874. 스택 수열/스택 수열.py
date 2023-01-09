import sys

n = int(input())
stack = list()
result = list()
cur = 1

for _ in range(n):
    data = int(sys.stdin.readline())
    while cur <= data:
        stack.append(cur)
        result.append('+')
        cur += 1
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        exit(0)

else:
    for i in result:
        print(i)
