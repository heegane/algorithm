import sys

sys.setrecursionlimit(10 ** 8)


def dfs(graph, v, visited):
    global count
    visited[v] = True
    answer[v - 1] = count
    count += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
answer = [0] * N
count = 1
for _ in range(M):
    first, second = sys.stdin.readline().rstrip().split()
    graph[int(first)].append(int(second))
    graph[int(second)].append(int(first))

for edge in graph:
    edge.sort(reverse=True)

dfs(graph, R, visited)

for result in answer:
    sys.stdout.write(str(result) + "\n")
