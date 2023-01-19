from collections import deque

B, C, D = map(int, input().split())
buger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))

buger.sort(reverse=True)
buger = deque(buger)
side.sort(reverse=True)
side = deque(side)
drink.sort(reverse=True)
drink = deque(drink)

print(sum(buger) + sum(side) + sum(drink))
result = 0

for _ in range(min(B, C, D)):
    result += (buger[0] + side[0] + drink[0]) * 0.9
    buger.popleft()
    side.popleft()
    drink.popleft()

result += sum(buger) + sum(side) + sum(drink)

print(int(result))
