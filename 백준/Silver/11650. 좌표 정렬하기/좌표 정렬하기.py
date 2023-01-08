import sys

N = int(input())

arr = []
arr_minus = []
arr_plus = []

for i in range(0, N):
    data = list(map(int, sys.stdin.readline().split()))
    arr.append(data)

arr.sort()

for i in range(0, N):
    print(f"{arr[i][0]} {arr[i][1]}")