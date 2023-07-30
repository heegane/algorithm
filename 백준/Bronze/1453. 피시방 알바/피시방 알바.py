import sys

n = int(sys.stdin.readline())
seats = list(map(int, sys.stdin.readline().rstrip().split()))
d = {}
cnt = 0

for seat in seats:
    if seat in d:
        cnt += 1
    else:
        d[seat] = True

sys.stdout.write(str(cnt))
