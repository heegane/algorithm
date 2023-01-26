import sys

N = int(input())
data = {}
arr = list(map(int, input().split()))
result = []

for i in range(N):
    if arr[i] in data:
        data[arr[i]] += 1
    else:
        data[arr[i]] = 1

M = int(input())
arr.clear()
arr = list(map(int, input().split()))

for i in range(M):
    if arr[i] in data:
        sys.stdout.write(str(data[arr[i]]) + " ")
    else:
        sys.stdout.write("0 ")
