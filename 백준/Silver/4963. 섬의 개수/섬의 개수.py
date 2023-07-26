import sys
from collections import deque

q = deque()


def bfs(x, y):
    # 대각선까지 고려
    dx = [-1, 1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]

    q = deque()
    q.append([x, y])

    while len(q) != 0:
        current = q.popleft()
        x, y = current[0], current[1]
        for i in range(8):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x and next_x < h and 0 <= next_y and next_y < w:
                if graph[next_x][next_y] == 1:
                    graph[next_x][next_y] = 0
                    q.append([next_x, next_y])


while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())

    if w == 0 and h == 0:
        break

    graph = []
    count = 0

    for i in range(h):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)
