import java.util.*;

class Solution {
    int[] visited;
    public int solution(int n, int[][] edge) {
        visited = new int[n+1];
        Map<Integer, List<Integer>> map = new HashMap<>();
        for(int i = 1; i <= n; i++) {
            map.put(i, new ArrayList<>());
        }
        for(int[] e : edge) {
            int a = e[0];
            int b = e[1];
            map.get(a).add(b);
            map.get(b).add(a);
        }
        
        bfs(1, map);
        
        int max = 1;
        int answer = 0;
        
        for(int i = 1; i <= n; i++) {
            if(max < visited[i]) {
                max = visited[i];
                answer = 1;
            }
            else if(max == visited[i]) {
                answer++;
            }
        }
        return answer;
    }
    
    public void bfs(int start, Map<Integer, List<Integer>> map) {
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(start);
        visited[start] = 1;
        
        while(!queue.isEmpty()) {
            int cur = queue.poll();
            for(int next : map.get(cur)) {
                if(visited[next] == 0) {
                    queue.add(next);
                    visited[next] = visited[cur] + 1;
                }
            }
        }
    }
}