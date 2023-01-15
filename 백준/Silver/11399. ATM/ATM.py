N = int(input())
p = list(map(int, input().split()))
p.sort()

result = 0

for i in range(N):
    result += sum(p[0:i + 1])

print(result)
