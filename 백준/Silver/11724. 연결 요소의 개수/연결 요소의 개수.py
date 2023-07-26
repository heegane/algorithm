import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]  # N개의 정점 인덱스 1부터 N까지
visited = [False] * (N + 1)  # N개의 정점 인덱스 1부터 N까지
stack = []

for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(graph, start):
    visited[start] = True
    stack.append(start)

    while len(stack) != 0:
        current = stack.pop()

        for next in graph[current]:
            if not visited[next]:
                visited[next] = True
                stack.append(next)


# 연결 요소(count)의 개수 = DFS 또는 BFS를 수행하는 횟수
count = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(graph, i)
        count += 1

sys.stdout.write(str(count))
