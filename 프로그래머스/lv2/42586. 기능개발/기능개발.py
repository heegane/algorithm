from collections import deque

def solution(progresses, speeds):
    answer = []
    # 큐로 초기화를 한다
    new_progresses = deque()
    new_speeds = deque()
    
    for progress in progresses:
        new_progresses.append(progress)
    for speed in speeds:
        new_speeds.append(speed)
    # 가장 앞에서부터 기능을 완성한다
    while(len(new_speeds) != 0):
        temp_progress = new_progresses.popleft()
        temp_speed = new_speeds.popleft()
        count = 1
        # 기능이 완성되는 날짜를 구한다
        day = ((100-temp_progress)//temp_speed)
        if((100-temp_progress)%temp_speed != 0):
            day = day + 1
        # 앞서 완성된 기능과 같이 완성되는 기능들을 찾는다
        while(len(new_speeds)!=0):
            f_progress = new_progresses[0]
            f_speed = new_speeds[0]
            # 앞서 구한 날짜를 기준으로 완성도가 100이 넘는 기능들을 전부 제거한다
            result = f_progress + (f_speed * day)
            if(result >= 100):
                new_progresses.popleft()
                new_speeds.popleft()
                count = count + 1
            else:
                break
        answer.append(count)
    return answer