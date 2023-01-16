N = int(input())
data = list(map(int, input().split()))

data = set(data)
data = list(data)
data.sort()

for i in range(len(data)):
    print(f"{data[i]} ", end='')
