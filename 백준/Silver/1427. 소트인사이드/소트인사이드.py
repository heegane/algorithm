import sys

data = sys.stdin.readline().rstrip()
result = []

for i in range(len(data)):
    result.append(int(data[i]))

result.sort(reverse=True)
result = map(str, result)
result = ''.join(result)
sys.stdout.write(result)
