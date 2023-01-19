N = int(input())
drink = list(map(int, input().split()))
drink.sort(reverse=True)
result = drink[0]

for i in range(1, N):
    result += drink[i] / 2
print(round(result, 1))
