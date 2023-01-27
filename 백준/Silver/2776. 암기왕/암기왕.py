import sys

T = int(input())

for _ in range(T):
    note_1 = {}
    N = int(sys.stdin.readline().rstrip())
    data = list(map(int, sys.stdin.readline().rstrip().split()))

    for i in range(len(data)):
        note_1[data[i]] = 1

    M = int(sys.stdin.readline().rstrip())
    find = list(map(int, sys.stdin.readline().rstrip().split()))

    for j in range(len(find)):
        if find[j] in note_1:
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
