from collections import deque

def solution(arr):
    answer = []
    
    deq = deque(arr)
    
    if len(answer) == 0:
        answer.append(deq[0])
        deq.popleft()
        
    for _ in range(len(deq)):
        if len(deq) == 0:
            break
            
        else: 
            if answer[-1] == deq[0]:
                deq.popleft()
            else:
                answer.append(deq[0])
                deq.popleft()
                
    return answer