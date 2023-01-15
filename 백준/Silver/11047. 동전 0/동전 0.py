import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
coin_list = list()
count = 0

for _ in range(N):
    data = int(sys.stdin.readline().rstrip())
    coin_list.append(data)

coin_list.sort(reverse=True)

for coin in coin_list:
    if K == 0:
        break

    if K >= coin:
        count += K // coin
        K %= coin
    else:
        continue

print(count)
