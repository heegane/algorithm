import sys

input = sys.stdin.readline

n = int(input())
answer = 0
h = {}

for _ in range(n):
    input_data = input().rstrip()
    if input_data == "ENTER":
        h = {}
    else:
        if input_data not in h:
            h[input_data] = 1
            answer += 1
print(answer)
