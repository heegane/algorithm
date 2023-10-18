from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []
    s = []
    n = len(prices)
    s.append(prices.popleft())
    
    while len(s) < n:
        cnt = 0
        for price in prices:
            if s[-1] <= price:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
        s.append(prices.popleft())
    answer.append(0)
    return answer