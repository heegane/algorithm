import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        Map<Integer, List<Integer>> map = new HashMap<>();
        for(int i = 1; i <= n; i++) {
            map.put(i, new ArrayList<>());
        }
        for(int[] wire : wires) {
            int v1 = wire[0];
            int v2 = wire[1];
            map.get(v1).add(v2);
            map.get(v2).add(v1);
        }
        
        for(int[] wire: wires) {
            Integer v1 = wire[0];
            Integer v2 = wire[1];
            map.get(v1).remove(v2);
            map.get(v2).remove(v1);
            
            boolean[] visited = new boolean[n+1];
            bfs(1, visited, map);
            
            int cnt = 0;
            for(int i = 1; i <= n; i++) {
                if(visited[i]) cnt++;
            }
            int cnt2 = n - cnt;
            answer = Math.min(answer, Math.abs(cnt-cnt2));
            
            map.get(v1).add(v2);
            map.get(v2).add(v1);
        }
        
        return answer;
    }
    
    public void bfs(int start, boolean[] visited, Map<Integer, List<Integer>> map) {
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(start);
        visited[start] = true;
        
        while(!queue.isEmpty()) {
            int cur = queue.poll();
            for(int next: map.get(cur)) {
                if(!visited[next]) {
                    queue.add(next);
                    visited[next] = true;
                }
            }
        }
    }
}