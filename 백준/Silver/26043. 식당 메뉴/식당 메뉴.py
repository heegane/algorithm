import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()
type_a = []
type_b = []
type_c = []

for i in range(0, N):
    s = sys.stdin.readline().split()
    type_value = int(s[0])

    if type_value == 1:
        first, second = int(s[1]), int(s[2])
        queue.append([first, second])
    else:
        first = int(s[1])  # first = b (학생이 좋아하는 메뉴)
        student = queue.popleft()
        if student[1] == first:
            type_a.append(student)

        elif student[1] != first:
            type_b.append(student)

for i in range(0, len(queue)):
    type_c.append(queue.popleft())

if len(type_a) > 0:
    type_a.sort()
    for i in range(0, len(type_a)):
        sys.stdout.write(f"{type_a[i][0]} ")
else:
    sys.stdout.write("None")

sys.stdout.write("\n")

if len(type_b) > 0:
    type_b.sort()
    for i in range(0, len(type_b)):
        sys.stdout.write(f"{type_b[i][0]} ")
else:
    sys.stdout.write("None")

sys.stdout.write("\n")

if len(type_c) > 0:
    type_c.sort()
    for i in range(0, len(type_c)):
        sys.stdout.write(f"{type_c[i][0]} ")
else:
    sys.stdout.write("None")