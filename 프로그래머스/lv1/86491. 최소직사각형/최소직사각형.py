def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            temp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = temp
    
    
    sizes.sort(key=lambda x:x[0],reverse=True)
    w = sizes[0][0]
    
    sizes.sort(key=lambda x:x[1],reverse=True)
    h = sizes[0][1]
    
    answer = w*h
    return answer