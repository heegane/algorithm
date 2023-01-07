import sys

N = int(sys.stdin.readline())

arr = []

for i in range(0, N):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for i in range(0, N):
    print(arr[i])