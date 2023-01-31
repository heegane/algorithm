S = input()
result = []

for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        result.append(S[i:j])

result = set(result)
print(len(result))
