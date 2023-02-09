import sys

N = int(input())

for i in range(N):
    stack = list(sys.stdin.readline().rstrip().split())
    sys.stdout.write("Case #" + str(i + 1) + ": ")
    for _ in range(len(stack)):
        sys.stdout.write(stack.pop() + " ")
    sys.stdout.write("\n")
    stack.clear()
