N = int(input())
answer = list(map(int, input().split()))
result = 0
bonus = 0

for i in range(N):
    if answer[i] == 1:
        bonus += 1
        result += bonus
    else:
        bonus = 0

print(result)
