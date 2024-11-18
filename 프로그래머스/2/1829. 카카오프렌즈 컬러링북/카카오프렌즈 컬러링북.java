import java.util.*;

class Solution {
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        
        int[][] visited = new int[m][n];
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(picture[i][j] != 0 && visited[i][j] == 0) {
                    numberOfArea++;
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, bfs(picture, visited, picture[i][j], new int[]{i,j}, m, n, numberOfArea));
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
    
    public int bfs(int[][] picture, int[][] visited, int type, int[] start, int m, int n, int area) {
        visited[start[0]][start[1]] = area;
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(start);
        int[] drs = {-1,1,0,0};
        int[] dcs = {0,0,-1,1};
        
        while(!queue.isEmpty()) {
            int[] cur = queue.poll();
            int r = cur[0];
            int c = cur[1];
            for(int i = 0; i < 4; i++) {
                int nextR = r + drs[i];
                int nextC = c + dcs[i];
                if(0 <= nextR && nextR < m && 0 <= nextC && nextC < n) {
                    if(picture[nextR][nextC] == type && visited[nextR][nextC] == 0) {
                        visited[nextR][nextC] = area;
                        queue.add(new int[]{nextR, nextC});
                    }
                }
            }
        }
        
        int result = 0;
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(visited[i][j] == area) {
                    result++;
                }
            }
        }
        return result;
    }
}