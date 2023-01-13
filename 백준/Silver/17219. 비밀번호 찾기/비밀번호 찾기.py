import sys

N, M = map(int, input().split())
d = {}
for _ in range(N):
    key, password = sys.stdin.readline().rstrip().split()
    d[key] = password

for _ in range(M):
    find = sys.stdin.readline().rstrip()
    print(d[find])
