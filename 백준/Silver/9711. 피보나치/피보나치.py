n = int(input())
x = 1
dp = [0 for _ in range(10001)]
dp[0], dp[1] = 0, 1

for i in range(2, 10001):
    dp[i] = dp[i - 1] + dp[i - 2]

for _ in range(0, n):
    arr = input().split()
    p, q = int(arr[0]), int(arr[1])
    print(f"Case #{x}: {dp[p] % q}")
    x += 1