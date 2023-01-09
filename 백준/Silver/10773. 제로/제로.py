import sys

K = int(input())

arr = list()
result = 0

for _ in range(K):
    data = int(sys.stdin.readline())
    if data != 0:
        arr.append(data)
    else:
        arr.pop()

for _ in range(len(arr)):
    result = result + arr.pop()

print(result)
