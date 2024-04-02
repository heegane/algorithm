import sys

input = sys.stdin.readline

n = int(input())

# 5의 배수인 경우
# 3의 배수인 경우
# 3과 5로 나눌 수 있는 경우
# 남은게 2 이하면 -1

if n % 5 == 0:
    print(n // 5)
else:
    answer = 0
    while n > 0:
        if n % 5 != 0:
            n -= 3
            answer += 1
        else:
            answer += n // 5
            n = n % 5

        if n == 1 or n == 2:
            print(-1)
            exit()
    print(answer)
