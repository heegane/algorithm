import sys

N, M = map(int, input().split())
words = {}
result = []
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) < M:
        continue
    else:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

for word in words:
    result.append((word, words[word], len(word)))

result = sorted(result, key=lambda x: (-x[1], -x[2], x))

for i in range(len(result)):
    sys.stdout.write(str(result[i][0]) + "\n")
