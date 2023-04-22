N = int(input())
tops = list(map(int, input().split()))
result = []
stack = []

for i in range(N):
    while stack:
        if stack[-1][1] > tops[i]:
            result.append(stack[-1][0])
            break
        else:
            stack.pop()
    if not stack:
        result.append(0)
    stack.append([i + 1, tops[i]])

answer = " ".join(map(str, result))
print(answer)
