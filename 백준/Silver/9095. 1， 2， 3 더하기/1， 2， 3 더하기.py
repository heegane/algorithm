import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    dp = [0] * (n + 1)
    if n == 1:
        sys.stdout.write(str(1) + "\n")
    elif n == 2:
        sys.stdout.write(str(2) + "\n")
    elif n == 3:
        sys.stdout.write(str(4) + "\n")
    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4

        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        sys.stdout.write(str(dp[n]) + "\n")
