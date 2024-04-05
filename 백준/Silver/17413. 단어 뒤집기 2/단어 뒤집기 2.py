import sys
from collections import deque

input = sys.stdin.readline

s = deque(input().rstrip())
stack = []
while s:

    if s[0] == '<' or s[0] == ' ':
        while stack:
            sys.stdout.write(stack.pop())

        if s[0] == ' ':
            sys.stdout.write(s.popleft())
        elif s[0] == '<':
            sys.stdout.write(s.popleft())
            while s[0] != '>':
                sys.stdout.write(s.popleft())
            sys.stdout.write(s.popleft())

    else:
        stack.append(s.popleft())

while stack:
    sys.stdout.write(stack.pop())
sys.stdout.write("\n")
