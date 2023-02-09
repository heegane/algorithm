import sys

T = int(input())

for _ in range(T):
    stack = []
    data = sys.stdin.readline().rstrip()
    for i in range(len(data)):
        if data[i] == '(':
            stack.append(data[i])
        else:
            if stack:
                stack.pop()
            else:
                sys.stdout.write("NO\n")
                break

    else:
        if stack:
            sys.stdout.write("NO\n")
        else:
            sys.stdout.write("YES\n")