import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    if n == 1:
        input_data = int(input())
        if m < input_data:
            print("1")
        else:
            print("0")
    else:
        li = list(map(int, input().split()))
        q = deque()
        for i in range(n):
            # (위치, 가중치)
            q.append((i, li[i]))

        out = False
        while q:
            flag = False
            for j in range(1, len(q)):
                if q[0][1] < q[j][1]:
                    flag = True
                    
            if flag == True:
                q.append(q.popleft())

            else:
                if q[0][0] == m:
                    q.popleft()
                    print(n - len(q))
                    out = True
                else:
                    q.popleft()

            if out == True:
                break
