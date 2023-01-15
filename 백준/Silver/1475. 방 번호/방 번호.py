nums = list(map(int, input()))
result = [0] * 10
count = 0

for num in nums:
    if num == 6 or num == 9:
        count += 1
    else:
        result[num] += 1

if count % 2 == 0:
    result[6] = count // 2
else:
    result[6] = count // 2 + 1

print(max(result))
