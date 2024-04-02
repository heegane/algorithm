t = int(input())
dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for _ in range(t):
    n = int(input())

    if n <= 10:
        print(dp[n - 1])
    else:
        dp = dp + [0] * (n - 10)

        for i in range(10, n):
            dp[i] = dp[i - 2] + dp[i - 3]
        print(dp[n - 1])
