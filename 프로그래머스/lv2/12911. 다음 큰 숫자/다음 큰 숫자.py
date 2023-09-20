def solution(n):
    answer = 0
    next_n = n + 1
    while True:
        if str(format(n,'b')).count('1') == str(format(next_n,'b')).count('1'):
            break
        else:
            next_n = next_n + 1
    
    answer = next_n
    return answer