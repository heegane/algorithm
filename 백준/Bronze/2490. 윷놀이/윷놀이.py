import sys

for _ in range(3):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    count = data.count(0)
    if count == 1:
        print("A")
    elif count == 2:
        print("B")
    elif count == 3:
        print("C")
    elif count == 4:
        print("D")
    else:
        print("E")
