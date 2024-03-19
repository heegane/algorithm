import sys

input = sys.stdin.readline

n = int(input())
dp = [0, 1, 3, 5, 11] + [0] * (n - 4)

if 1 <= n <= 4:
    print(dp[n] % 10007)
else:
    for i in range(5, n + 1):
        dp[i] = dp[i - 2] * 2 + dp[i - 1]
    print(dp[n] % 10007)
