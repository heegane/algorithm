import sys

K, L = map(int, input().split())
students = {}

for _ in range(L):
    data = sys.stdin.readline().rstrip()
    if data in students:
        del students[data]
        students[data] = 1
    else:
        students[data] = 1

students = list(students)

if len(students) >= K:
    for i in range(K):
        sys.stdout.write(students[i] + "\n")
else:
    for i in range(len(students)):
        sys.stdout.write(students[i] + "\n")
