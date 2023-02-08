import sys

T = int(input())
for _ in range(T):
    result = 0
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    data = [[0 for col in range(n)] for row in range(k)]

    for i in range(n):
        data[0][i] = i + 1

    for i in range(1, k):
        for j in range(n):
            for z in range(j + 1):
                data[i][j] += data[i - 1][z]

    for i in range(n):
        result += data[k - 1][i]
    sys.stdout.write(str(result) + "\n")
    data.clear()
