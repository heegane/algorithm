import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s, p = input().split()
    answer = 0
    answer += s.count(p)
    s = s.replace(p, '', answer)
    answer += len(s)
    print(answer)
