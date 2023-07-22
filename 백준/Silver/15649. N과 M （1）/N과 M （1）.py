n, m = map(int,input().split())

num = [i+1 for i in range(n)]
visited = [False] * n
answer = []

def dfs(cnt):
    # print(answer)
    if cnt == m:
        print(*answer)
        return
    for i in range(n):
        if visited[i] == True:
            continue
        visited[i] = True
        answer.append(num[i])
        dfs(cnt+1)
        answer.pop()
        visited[i] = False
dfs(0)