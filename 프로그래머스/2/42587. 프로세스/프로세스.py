from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque()
    for i in range(len(priorities)):
        # (location, priorities)
        q.append((i, priorities[i]))
    
    while q:
        flag = True
        for i in range(1, len(q)):
            if q[0][1] < q[i][1]:
                q.append(q.popleft())
                flag = False
                break
        if flag == True:
            if q[0][0] == location:
                q.popleft()
                answer += 1
                break
            else:
                q.popleft()
                answer += 1
    
    return answer