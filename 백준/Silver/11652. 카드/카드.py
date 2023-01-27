import sys

card = {}
n = int(input())
for _ in range(n):
    data = int(sys.stdin.readline().rstrip())
    if data in card:
        card[data] += 1
    else:
        card[data] = 1

card = sorted(card.items(), key=lambda x: (-x[1], x[0]))
sys.stdout.write(str(card[0][0]) + "\n")
