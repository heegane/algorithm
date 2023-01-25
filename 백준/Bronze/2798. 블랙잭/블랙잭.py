from itertools import combinations

N, M = map(int, input().split())
card = list(map(int, input().split()))
result = []

for three in combinations(card, 3):
    if sum(three) > M:
        continue
    else:
        result.append(sum(three))

print(max(result))
