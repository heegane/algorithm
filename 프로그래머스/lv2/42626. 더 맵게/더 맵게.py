import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            break
        else:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)*2
            heapq.heappush(scoville,first+second)
            count += 1
        
    if scoville[0] < K:
        return -1
    
    answer = count
    return answer