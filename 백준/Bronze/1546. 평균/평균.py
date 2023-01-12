score = list()

N = int(input())
arr = input().split()

for i in range(0, N):
    score.append(int(arr[i]))

score.sort()
score.reverse()
M = score[0]

for i in range(0, N):
    score[i] = score[i] / M * 100

print(sum(score) / N)
