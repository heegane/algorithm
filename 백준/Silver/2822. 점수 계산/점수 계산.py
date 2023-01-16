import sys

score = []
result = 0
for i in range(8):
    data = int(sys.stdin.readline().rstrip())
    score.append([data, i + 1])

score.sort(reverse=True)
for _ in range(3):
    score.pop()

for i in range(len(score)):
    result += score[i][0]
print(result)

score.sort(key=lambda x: (x[1]))

for i in range(len(score)):
    print(f"{score[i][1]} ", end='')
