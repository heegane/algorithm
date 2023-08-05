import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

#간선을 관리할 인접 리리스스트  생생성성
graph = [[] for y in range(n+1)]
for _ in range(m) :
    i, j, k = map(int, input().split())
    graph[i].append((j, k))

# 거리를 표시할 방문 배열 생성
# 1e9로 모든 거리 초기화
visit = [INF] * (n+1)

start, end = map(int, input().split())

def dijkstra(start) :
    heap = []
    # 시작점의 방문 거리를 0으로 초기화
    visit[start] = 0
    # 힙에는 [현재까지 거리, 현재 노드의 번호]를 삽입
    heapq.heappush(heap, (0, start))

    # 힙이 빌 때까지 수행
    while heap :
        dist, curr_node = heapq.heappop(heap)
        # 현재 노드의 방문 값이 dist보다 작으면 방문을 수행하지 않음
        if visit[curr_node] < dist :
            continue
        # 현재 노드와 연결된 다른 노드들까지의 방문 거리 값을 새로 갱신함
        for next_info in graph[curr_node] :
            cost = dist + next_info[1]
            next_node = next_info[0]
            # 만약 cost가 visit[next_node]보다 크거나 같다면
            # 이전에 다른 방법으로 방문하는 방법이 더 빠르기 때문에 수행하지 않음
            if cost < visit[next_node] :
                visit[next_node] = cost
                heapq.heappush(heap, (cost, next_node))

dijkstra(start)
print(visit[end])