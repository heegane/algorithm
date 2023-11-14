T = int(input())

for test_case in range(1, T + 1):
    N, D = map(int, input().split())
    result = 0
    cnt = 1
    D = D * 2 + 1
    for i in range(N):
        if cnt == D:
            cnt = 1
            result += 1
        else:
            cnt += 1
    if cnt != 1:
        result += 1
    print("#%d %d" % (test_case, result))
