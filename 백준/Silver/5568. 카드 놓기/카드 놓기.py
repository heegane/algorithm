import itertools
import sys

n = int(input())
k = int(input())
card = []
for _ in range(n):
    card.append(sys.stdin.readline().rstrip())

result = set(map(''.join, itertools.permutations(card, k)))
print(len(result))
