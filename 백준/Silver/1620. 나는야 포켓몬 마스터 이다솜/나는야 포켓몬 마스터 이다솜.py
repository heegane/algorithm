import sys

N, M = map(int, input().split())
data = {}
for i in range(1, N + 1):
    input_data = sys.stdin.readline().rstrip()
    data[input_data] = i
    data[i] = input_data

for _ in range(M):
    find = sys.stdin.readline().rstrip()
    if find.isdigit():
        sys.stdout.write(str(data[int(find)]) + "\n")
    else:
        sys.stdout.write(str(data[find]) + "\n")
