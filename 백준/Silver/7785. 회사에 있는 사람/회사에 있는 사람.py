import sys

people = {}
n = int(input())
for _ in range(n):
    name, status = sys.stdin.readline().rstrip().split()
    if name in people:
        del people[name]
    else:
        people[name] = status
people = set(people)
people = sorted(people, reverse=True)

for i in range(len(people)):
    sys.stdout.write(people[i] + "\n")
