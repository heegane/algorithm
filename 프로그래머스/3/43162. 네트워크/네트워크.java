import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        for(int i = 0; i < n; i++) {
            if(!visited[i]) {
                bfs(i, visited, computers);
                answer++;
            }
        }
        return answer;
    }
    
    public void bfs(int start, boolean[] visited, int[][] computers) {
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(start);
        visited[start] = true;
        
        while(!queue.isEmpty()) {
            int cur = queue.poll();
            for(int next = 0; next < computers[cur].length; next++) {
                if(!visited[next] && computers[cur][next] == 1) {
                    queue.add(next);
                    visited[next] = true;
                }
            }
        }
    }
}