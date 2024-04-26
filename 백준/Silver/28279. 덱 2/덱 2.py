import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    input_data = input().rstrip()
    if len(input_data) > 1:
        command, data = map(int, input_data.split())

        if command == 1:
            q.appendleft(data)
        elif command == 2:
            q.append(data)

    else:
        input_data = int(input_data)
        if input_data == 3:
            if q:
                sys.stdout.write(str(q.popleft()) + "\n")
            else:
                sys.stdout.write("-1" + "\n")
        elif input_data == 4:
            if q:
                sys.stdout.write(str(q.pop()) + "\n")
            else:
                sys.stdout.write("-1" + "\n")
        elif input_data == 5:
            sys.stdout.write(str(len(q)) + "\n")
        elif input_data == 6:
            if q:
                sys.stdout.write("0" + "\n")
            else:
                sys.stdout.write("1" + "\n")
        elif input_data == 7:
            if q:
                sys.stdout.write(str(q[0]) + "\n")
            else:
                sys.stdout.write("-1" + "\n")
        elif input_data == 8:
            if q:
                sys.stdout.write(str(q[-1]) + "\n")
            else:
                sys.stdout.write("-1" + "\n")
