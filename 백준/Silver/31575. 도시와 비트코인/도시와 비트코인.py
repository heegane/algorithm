import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(m):
    graph.append(list(map(int, input().split())))


def bfs(r, c):
    visited[r][c] = 1
    q = deque()
    q.append((r, c))

    dx = [1, 0]
    dy = [0, 1]

    while q:
        r, c = q.popleft()
        for i in range(2):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < m and 0 <= nc < n and visited[nr][nc] == 0 and graph[nr][nc] == 1:
                visited[nr][nc] = 1
                q.append((nr, nc))


bfs(0, 0)
if visited[-1][-1] == 1:
    print("Yes")
else:
    print("No")
