def solution(participant, completion):
    h = {}
    
    for p in participant:
        if p in h:
            h[p] += 1
        else:
            h[p] = 1
    
    for c in completion:
        if c in h:
            h[c] -= 1
    
    for key in h:
        if h[key] == 1:
            answer = key
            break
    return answer