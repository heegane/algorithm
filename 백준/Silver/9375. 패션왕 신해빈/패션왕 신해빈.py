import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    d = {}
    n = int(input())

    for _ in range(n):
        name, type = input().split()

        if type in d:
            d[type] += 1
        else:
            d[type] = 1

    answer = 1
    for i in d:
        answer *= (d[i] + 1)

    sys.stdout.write(str(answer - 1) + "\n")
