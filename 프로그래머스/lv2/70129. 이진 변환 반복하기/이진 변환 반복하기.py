def solution(s):
    answer = []
    cnt, zero_cnt = 0, 0
    
    while True:
        if s == '1':
            break
            
        zero_cnt = s.count('0') + zero_cnt
        s = s.replace('0','')
        c = len(s)
        s = format(c,'b')
        cnt = cnt + 1
    
    answer.append(cnt)
    answer.append(zero_cnt)
    return answer