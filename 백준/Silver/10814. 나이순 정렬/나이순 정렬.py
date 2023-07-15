import sys

N = int(sys.stdin.readline())

arr = []

for i in range(0, N):
    input_value = sys.stdin.readline().split()
    age, name = int(input_value[0]), input_value[1]
    arr.append([age, name])

arr.sort(key=lambda x: x[0])

for i in range(0, N):
    sys.stdout.write(f"{arr[i][0]} {arr[i][1]}\n")
