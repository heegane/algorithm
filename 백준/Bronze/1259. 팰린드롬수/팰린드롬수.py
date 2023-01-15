import sys

while True:
    data = sys.stdin.readline().rstrip()
    if data == '0':
        break
    else:
        if data == data[::-1]:
            print("yes")
        else:
            print("no")
