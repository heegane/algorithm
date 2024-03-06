import sys

input = sys.stdin.readline

n, x = map(int, input().split())
datas = list(map(int, input().split()))

left, right = 0, x
cur_v = sum(datas[0:x])
max_v = cur_v
cnt = 1

while right < n:

    cur_v = cur_v - datas[left] + datas[right]
    left += 1
    right = left + x

    if max_v == cur_v:
        cnt += 1

    if max_v < cur_v:
        max_v = cur_v
        cnt = 1

if max_v == 0:
    print("SAD")
else:
    print(max_v)
    print(cnt)
