import itertools

N = int(input())
nums = []
for i in range(1, N + 1):
    nums.append(int(i))

result = list(map(' '.join, itertools.permutations(map(str, nums))))

for i in range(len(result)):
    print(result[i])
