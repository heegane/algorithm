import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()

    if s == '*':
        exit()

    n = len(s)
    flag = 0

    if n == 1 or n == 2:
        sys.stdout.write(s + " is surprising." + "\n")
        continue

    for d in range(0, n - 1):
        flag = 0
        h = {}
        for i in range(0, n - 1 - d):
            word = s[i] + s[i + 1 + d]
            if word in h:
                flag = 1
                break
            else:
                h[word] = 1
        if flag == 1:
            sys.stdout.write(s + " is NOT surprising." + "\n")
            break
    if flag == 0:
        sys.stdout.write(s + " is surprising." + "\n")
