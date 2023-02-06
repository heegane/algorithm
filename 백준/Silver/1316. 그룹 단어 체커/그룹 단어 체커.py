import sys

N = int(input())
result = 0
words = {}

for _ in range(N):
    isGroup = True
    data = sys.stdin.readline().rstrip()
    words[data[0]] = 1
    for i in range(0, len(data) - 1):
        if data[i] != data[i + 1]:
            if data[i + 1] in words:
                isGroup = False
                break
            else:
                words[data[i]] = 1
                continue
        else:
            continue

    if isGroup is True:
        result += 1
    words.clear()

sys.stdout.write(str(result))
