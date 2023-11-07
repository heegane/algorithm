T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    datas = list(map(int, input().split()))
    result = 0
    datas.reverse()

    start = datas[0]
    buy = 0
    cnt = 0

    for i in range(1, N):
        if start > datas[i]:
            buy += datas[i]
            cnt += 1
        else:
            result += start * cnt - buy
            buy = 0
            cnt = 0
            start = datas[i]
    result += start * cnt - buy
    print("#%d %d" % (test_case, result))
