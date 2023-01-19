import sys

while True:
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    if data[0] == 0 and data[1] == 0 and data[2] == 0:
        exit(0)
    else:
        data.sort(reverse=True)
        if pow(data[0], 2) == pow(data[1], 2) + pow(data[2], 2):
            print("right")
        else:
            print("wrong")
