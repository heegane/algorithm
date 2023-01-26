import sys


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


N = int(input())
data = list(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))

data.sort()
for i in range(M):
    result = binary_search(data, find[i], 0, N - 1)
    if result is None:
        sys.stdout.write("0\n")
    else:
        sys.stdout.write("1\n")
