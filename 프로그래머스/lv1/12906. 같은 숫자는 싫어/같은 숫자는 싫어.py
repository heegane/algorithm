def solution(arr):
    answer = []
    
    for number in arr:
        if len(answer) == 0:
            answer.append(number)
            del arr[0]
        else:
            if answer[-1] == number:
                del arr[0]
                 
    return answer