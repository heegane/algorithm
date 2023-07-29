def solution(people, limit):
    # 정렬
    people.sort()
    # 구명 보트를 몇번 태우는가?
    answer = 0
    # 현재 가장 가벼운 사람의 위치 (시간복잡도를 줄이기 위해, remove하는 것보다 현저하게 시간 줄어든다)
    idx = 0
    
    # 현재 가벼운 사람의 위치가 배열의 크기를 벗어난다면, 모든 사람을 탐색한 것이므로 탐색 종료
    while len(people) > idx:
        # 가장 무거운 사람 무게
        back = people.pop()
        answer += 1
        # pop 때문에 한번 더 확인
        if len(people) <= idx:
            break
        # 가장 가벼운 사람과 무거운 사람의 합이 limit를 넘는지 확인
        if people[idx] + back <= limit:
            idx += 1
    
    return answer