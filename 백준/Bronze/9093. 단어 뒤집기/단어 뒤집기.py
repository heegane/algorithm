import sys

T = int(input())
for _ in range(T):
    S = list(sys.stdin.readline().rstrip().split())
    for word in S:
        print(f"{word[::-1]} ", end='')
    print()
