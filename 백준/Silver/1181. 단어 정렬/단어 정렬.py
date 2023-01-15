import sys

info = []
N = int(input())
for _ in range(N):
    data = sys.stdin.readline().rstrip()
    info.append(data)

info = set(info)
info = list(info)

info.sort(key=lambda x: (len(x), x))

for i in range(len(info)):
    print(info[i])
