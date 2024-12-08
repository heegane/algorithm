import java.util.*;

class Solution {
    List<String> candidates;
    
    public String[] solution(String[][] tickets) {
        List<String> answer = new ArrayList<>();
        candidates = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();
        
        // 1. 그래프 구성 및 정렬
        for (String[] ticket : tickets) {
            String start = ticket[0];
            String end = ticket[1];
            map.putIfAbsent(start, new ArrayList<>());
            map.get(start).add(end);
        }

        // 도착지 리스트를 사전순으로 정렬
        for (List<String> destinations : map.values()) {
            Collections.sort(destinations);
        }
        
        // 2. DFS 탐색 시작
        LinkedList<String> path = new LinkedList<>();
        path.add("ICN");
        dfs("ICN", tickets.length + 1, map, path);

        // 3. 최종 경로 반환
        return candidates.get(0).split(" ");
    }

    public void dfs(String current, int totalTickets, Map<String, List<String>> map, LinkedList<String> path) {
        // 모든 티켓 사용 시 경로 추가
        if (path.size() == totalTickets) {
            candidates.add(String.join(" ", path));
            return;
        }

        // 도착지 탐색
        if (map.containsKey(current)) {
            List<String> destinations = map.get(current);
            for (int i = 0; i < destinations.size(); i++) {
                String next = destinations.remove(i); // 방문 처리
                path.add(next);
                
                dfs(next, totalTickets, map, path);
                
                // 백트래킹
                path.removeLast();
                destinations.add(i, next);
            }
        }
    }
}
