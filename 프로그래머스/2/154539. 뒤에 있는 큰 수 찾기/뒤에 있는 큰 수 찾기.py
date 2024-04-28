def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for idx, num in enumerate(numbers):
        # 큰 수가 나온 경우, 그 수를 사용해 정답 정보 갱신
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(idx)
    
    return answer