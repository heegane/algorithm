def solution(s):
    answer = ''
    index = 0
    for i in range(len(s)):
        
        if s[i] == ' ':
            index = 0
            answer += s[i]
            continue
        
        if index % 2 == 0 or index == 0:
            answer += s[i].upper()
        else:
            answer += s[i].lower()
        index += 1
            
    return answer