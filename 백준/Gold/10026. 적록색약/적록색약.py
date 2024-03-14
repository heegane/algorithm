import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input()))


def see_RGB(x, y, color, flag):
    can_see_visited[x][y] = 1
    q = deque()
    q.append((x, y))
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    if flag == 0:
        can_see_visited[x][y] = 1
    else:
        cannot_see_visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dxs[i]
            ny = y + dys[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 적록색약 X
                if flag == 0:
                    if can_see_visited[nx][ny] == 0 and graph[nx][ny] == color:
                        can_see_visited[nx][ny] = 1
                        q.append((nx, ny))
                # 적록색약 O
                else:
                    if cannot_see_visited[nx][ny] == 0:
                        if ((color == 'R' or color == 'G') and (graph[nx][ny] == 'R' or graph[nx][ny] == 'G')) or (
                                color == 'B' and graph[nx][ny] == 'B'):
                            cannot_see_visited[nx][ny] = 1
                            q.append((nx, ny))


can_see_cnt = 0
can_see_visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (graph[i][j] == 'R' or graph[i][j] == 'G' or graph[i][j] == 'B') and can_see_visited[i][j] == 0:
            see_RGB(i, j, graph[i][j], 0)
            can_see_cnt += 1

cannot_see_cnt = 0
cannot_see_visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if (graph[i][j] == 'R' or graph[i][j] == 'G' or graph[i][j] == 'B') and cannot_see_visited[i][j] == 0:
            see_RGB(i, j, graph[i][j], 1)
            cannot_see_cnt += 1

sys.stdout.write(str(can_see_cnt) + " " + str(cannot_see_cnt) + "\n")
