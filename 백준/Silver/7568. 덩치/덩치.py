import sys

N = int(input())
people = []

for i in range(1, N + 1):
    weight, height = map(int, sys.stdin.readline().rstrip().split())
    people.append((weight, height))

for person1 in people:
    rank = 1
    for person2 in people:
        if person1[0] < person2[0] and person1[1] < person2[1]:
            rank += 1
    sys.stdout.write(str(rank) + " ")
