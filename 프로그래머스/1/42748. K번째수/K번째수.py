def solution(array, commands):
    answer = []
    
    for c in commands:
        x = c[0]
        y = c[1]
        z = c[2]
        
        li = []
        for j in range(x-1, y):
            li.append(array[j])
            
        li.sort()
        answer.append(li[z-1])
    return answer