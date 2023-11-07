T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    submit_nums = list(map(int, input().split()))
    print("#%d" % test_case, end=" ")
    for i in range(1, N + 1):
        if i not in submit_nums:
            print(i, end=" ")
    print()
