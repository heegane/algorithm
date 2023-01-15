import sys

info = []
N = int(input())
for _ in range(N):
    data = list(sys.stdin.readline().rstrip().split())
    info.append(data)

info.sort(key=lambda x: (-int(x[3]), -int(x[2]), -int(x[1])))
print(info[0][0])
print(info[-1][0])
