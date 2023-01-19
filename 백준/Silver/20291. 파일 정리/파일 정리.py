import sys
from collections import Counter

N = int(input())
data = []
for _ in range(N):
    front, back = sys.stdin.readline().rstrip().split('.')
    data.append(back)

result = Counter(data).most_common()
result = sorted(result, key=lambda x: x[0])

for i in range(len(result)):
    print(f"{result[i][0]} {result[i][1]}")
