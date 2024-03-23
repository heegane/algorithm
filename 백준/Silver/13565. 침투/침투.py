import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))


def bfs(x, y):
    visited[x][y] = 1
    q = deque()
    q.append((x, y))

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dxs[i]
            ny = y + dys[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))


for i in range(m):
    if graph[0][i] == 0 and visited[0][i] == 0:
        bfs(0, i)

if visited[- 1].count(1) > 0:
    print("YES")
else:
    print("NO")
