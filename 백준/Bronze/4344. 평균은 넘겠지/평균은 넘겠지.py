import sys

C = int(input())

for _ in range(C):
    scores = list(map(int, sys.stdin.readline().rstrip().split()))
    avg = sum(scores[1:]) / scores[0]
    cnt = 0
    for i in scores[1:]:
        if i > avg:
            cnt += 1
    rate = cnt / scores[0] * 100
    print(f"{rate:.3f}%")
