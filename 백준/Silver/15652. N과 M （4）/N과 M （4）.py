import sys

n, m = map(int,sys.stdin.readline().rstrip().split())
s = []

def dfs(start):
    if len(s) == m:
        sys.stdout.write(' '.join(map(str,s))+"\n")
        return

    for i in range(start,n+1):
        s.append(i)
        dfs(i)
        s.pop()

dfs(1)