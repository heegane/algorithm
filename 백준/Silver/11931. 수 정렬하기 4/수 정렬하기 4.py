import sys
n = int(sys.stdin.readline())

arr = []

for i in range(0,n):
    arr.append(int(sys.stdin.readline()))

arr.sort()
arr.reverse()

for i in range(0,n):
    print(arr[i])