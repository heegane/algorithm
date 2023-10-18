def solution(answers):
    answer = []
    li_1 = [1,2,3,4,5]
    li_2 = [2,1,2,3,2,4,2,5]
    li_3 = [3,3,1,1,2,2,4,4,5,5]
    index = [0] * 4
    cnt = [0] * 4
    
    for ans in answers:
        if ans == li_1[index[1]%5]:
            cnt[1] += 1
        if ans == li_2[index[2]%8]:
            cnt[2] += 1
        if ans == li_3[index[3]%10]:
            cnt[3] += 1
        index[1] += 1
        index[2] += 1
        index[3] += 1
        
    result = []
    result.append([cnt[1],1])
    result.append([cnt[2],2])
    result.append([cnt[3],3])
    result.sort(reverse=True)
    print(result)
    
    if result[0][0] == result[1][0]:
        answer.append(result[0][1])
        answer.append(result[1][1])
        if result[0][0] == result[2][0]:
            answer.append(result[2][1])
    else:
        answer.append(result[0][1])
    answer.sort()
    return answer