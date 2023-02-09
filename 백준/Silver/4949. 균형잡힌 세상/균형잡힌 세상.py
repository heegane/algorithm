import sys

while True:
    stack = []
    data = sys.stdin.readline().rstrip()
    if data[0] == '.' and len(data) == 1:
        break
    else:
        for i in range(len(data)):
            if data[i] == '(' or data[i] == '[':
                stack.append(data[i])
            else:
                if data[i] == ')':
                    if stack:
                        if stack[-1] == '(':
                            stack.pop()
                        else:
                            sys.stdout.write("no\n")
                            break
                    else:
                        sys.stdout.write("no\n")
                        break

                elif data[i] == ']':
                    if stack:
                        if stack[-1] == '[':
                            stack.pop()
                        else:
                            sys.stdout.write("no\n")
                            break
                    else:
                        sys.stdout.write("no\n")
                        break
        else:
            if stack:
                sys.stdout.write("no\n")
            else:
                sys.stdout.write("yes\n")
