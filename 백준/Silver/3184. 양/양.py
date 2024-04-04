import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
graph = []

for _ in range(r):
    graph.append(list(input().rstrip()))


def bfs(x, y, visited):
    lamb, woof = 1, 0
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
            # r, c 범위 헷갈려서 시간 걸림
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny] != '#':
                if graph[nx][ny] == 'o':
                    lamb += 1
                elif graph[nx][ny] == 'v':
                    woof += 1
                visited[nx][ny] = 1
                q.append((nx, ny))

    if lamb > woof:
        woof = 0
    else:
        lamb = 0
    return (lamb, woof)


visited = [[0] * c for _ in range(r)]
lamb = 0
woof = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'o' and not visited[i][j]:
            result = bfs(i, j, visited)
            lamb += result[0]
            woof += result[1]

for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            if graph[i][j] == 'o':
                lamb += 1
            elif graph[i][j] == 'v':
                woof += 1
sys.stdout.write(str(lamb) + " " + str(woof) + "\n")
