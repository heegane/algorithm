n = int(input())
dp = [0 for _ in range(10001)]
dp[0], dp[1], dp[2] = 0, 1, 1

for i in range(3,n+1):
    dp[i] = dp[i-2]+dp[i-1]
print(dp[n])