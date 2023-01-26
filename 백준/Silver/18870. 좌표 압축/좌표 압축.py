import sys

N = int(input())
data = list(map(int, input().split()))
data_set = set(data)
data_sort = sorted(data_set)
result = {}

for i in range(len(data_set)):
    result[data_sort[i]] = i

for i in range(N):
    sys.stdout.write(str(result[data[i]]) + " ")
