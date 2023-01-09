import sys

T = int(input())

for _ in range(T):
    R, S = sys.stdin.readline().split()
    size = len(S)
    for i in range(0, size):
        for _ in range(int(R)):
            sys.stdout.write(S[i])
    print()
