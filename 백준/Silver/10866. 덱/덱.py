import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()

for i in range(N):
    input_arr = sys.stdin.readline().split()
    command = input_arr[0]
    if command == "push_back":
        value = int(input_arr[1])
        queue.append(int(value))
    elif command == "push_front":
        value = int(input_arr[1])
        queue.appendleft(int(value))
    else:
        if command == "pop_front":
            if len(queue) == 0:
                print(-1)
            else:
                pop_value = queue.popleft()
                print(pop_value)
        elif command == "pop_back":
            if len(queue) == 0:
                print(-1)
            else:
                pop_value = queue.pop()
                print(pop_value)
        elif command == "size":
            print(len(queue))
        elif command == "empty":
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif command == "front":
            if len(queue) == 0:
                print(-1)
            else:
                print(f"{queue[0]}")
        elif command == "back":
            size = len(queue)
            if size == 0:
                print(-1)
            else:
                print(f"{queue[size - 1]}")
