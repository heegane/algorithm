import sys

book = {}
N = int(input())

for _ in range(N):
    data = sys.stdin.readline().rstrip()
    if data in book:
        book[data] += 1
    else:
        book[data] = 1

book = sorted(book.items(), key=lambda x: (-x[1], x[0]))
print(book[0][0])
