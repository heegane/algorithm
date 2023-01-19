N = int(input())
price = []
for _ in range(N):
    data = int(input())
    price.append(data)
price.sort(reverse=True)

result = 0
for i in range(N):
    if i % 3 == 2:
        continue
    else:
        result += price[i]
print(result)
