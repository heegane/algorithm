import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    j, n = map(int, input().split())
    boxes = []
    for _ in range(n):
        r, c = map(int, input().split())
        boxes.append(r * c)

    boxes.sort(reverse=True)

    answer = 0

    for box in boxes:
        j -= box
        answer += 1

        if j <= 0:
            break
            
    print(answer)
