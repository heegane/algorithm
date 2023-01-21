import sys


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


computer_nums = int(input())
network_nums = int(input())

graph = [[] for _ in range(computer_nums + 1)]

for _ in range(network_nums):
    first, second = sys.stdin.readline().rstrip().split()
    graph[int(first)].append(int(second))
    graph[int(second)].append(int(first))

visited = [False] * (computer_nums + 1)

dfs(graph, 1, visited)
print(visited.count(True) - 1)
