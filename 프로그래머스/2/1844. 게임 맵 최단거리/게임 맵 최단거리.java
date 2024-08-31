import java.util.*;

class Solution {
    int n;
    int m;
    int[][] visited;
    public int solution(int[][] maps) {
        n = maps.length;
        m = maps[0].length;
        visited = new int[n][m];
        bfs(0, 0, maps);
        return visited[n-1][m-1] == 0 ? -1 : visited[n-1][m-1];
    }
    
    public void bfs(int startR, int startC, int[][] maps) {
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{startR, startC});
        visited[startR][startC] = 1;
        
        int[] drs = {-1,1,0,0};
        int[] dcs = {0,0,-1,1};
        
        while(!queue.isEmpty()) {
            int[] cur = queue.poll();
            int r = cur[0];
            int c = cur[1];
            
            for(int i = 0; i < 4; i++) {
                int nr = r + drs[i];
                int nc = c + dcs[i];
                if(0 <= nr && nr < n && 0 <= nc && nc < m && visited[nr][nc] == 0 && maps[nr][nc] == 1) {
                    queue.add(new int[]{nr,nc});
                    visited[nr][nc] = visited[r][c] + 1;
                }
            }
        }
    }
}