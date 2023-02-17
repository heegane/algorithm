import sys

N, M = map(int, input().split())
keyword = {}

for _ in range(N):
    data = sys.stdin.readline().rstrip()
    keyword[data] = 1

keyword_copy = keyword
for _ in range(M):
    data = list(sys.stdin.readline().rstrip().split(','))
    for word in data:
        if word in keyword_copy:
            del keyword_copy[word]
        else:
            continue
    sys.stdout.write(str(len(keyword_copy)) + "\n")
    keyword_copy = keyword
