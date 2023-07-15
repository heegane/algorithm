def solution(nums):
    type = {}
    answer = 0
    
    for num in nums:
        if num in type:
            continue
        else:
            type[num] = 'o'
            answer += 1
        
    return min(answer,len(nums)//2)