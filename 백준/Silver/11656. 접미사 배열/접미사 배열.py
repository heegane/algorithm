S = input()
data = []

for i in range(len(S)):
    data.append(S[i:])

data.sort()

for i in range(len(S)):
    print(data[i])
