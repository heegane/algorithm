from collections import deque

for test_case in range(1, 11):
    n, string = input().split()
    n = int(n)
    string = deque(list(string))
    stack = []

    stack.append(string.popleft())
    while len(string) != 0:
        if len(stack) == 0:
            stack.append(string.popleft())
        else:
            if stack[-1] == string[0]:
                stack.pop()
                string.popleft()
            else:
                stack.append(string.popleft())
    print("#%d" % test_case, end=" ")
    print(''.join(stack))
