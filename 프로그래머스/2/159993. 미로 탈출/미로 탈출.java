import java.util.*;

class Solution {
    int n;
    int m;
    char[][] graph;
    public int solution(String[] maps) {
        int answer = 0;
        n = maps.length;
        m = maps[0].length();
        int[] start = new int[2];
        int[] lever = new int[2];
        int[] end = new int[2];
        graph = new char[n][m];
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                char c = maps[i].charAt(j);
                if(c == 'S') {
                    start[0] = i;
                    start[1] = j;
                }
                if(c == 'L') {
                    lever[0] = i;
                    lever[1] = j;
                }
                if(c == 'E') {
                    end[0] = i;
                    end[1] = j;
                }
                graph[i][j] = c;
            }
        }
        int sl = bfs(start, lever);
        if(sl == -1) {
            return -1;
        } else {
            answer += sl;
        }
        int le = bfs(lever, end);
        if(le == -1) {
            return -1;
        } else {
            answer += le;
        }
        return answer;
    }
    
    public int bfs(int[] start, int[] target) {
        boolean[][] visited = new boolean[n][m];
        visited[start[0]][start[1]] = true;
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{start[0], start[1], 0});
        
        while(!queue.isEmpty()) {
            int[] cur = queue.poll();
            int r = cur[0];
            int c = cur[1];
            int d = cur[2];
            int[] drs = {-1, 1, 0, 0};
            int[] dcs = {0, 0, -1, 1};
            for(int i = 0; i < 4; i++) {
                int nextR = r + drs[i];
                int nextC = c + dcs[i];
                if(0 <= nextR && nextR < n && 0 <= nextC && nextC < m) {
                    if(!visited[nextR][nextC] && graph[nextR][nextC] != 'X') {
                        if(nextR == target[0] && nextC == target[1]) {
                            return d + 1;
                        } else {
                            queue.add(new int[]{nextR, nextC, d + 1});
                            visited[nextR][nextC] = true;
                        }
                    }
                }
            }
        }
        return -1;
    }
}