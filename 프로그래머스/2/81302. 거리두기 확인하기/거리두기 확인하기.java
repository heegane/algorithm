import java.util.*;

class Solution {
    public int[] solution(String[][] places) {
        int[] answer = {1,1,1,1,1};
        
        for(int i = 0; i < 5; i++) {
            String[] place = places[i];
            char[][] graph = createGraph(place);
            
            for(int j = 0; j < 5; j++) {
                for(int z = 0; z < 5; z++) {
                    if(graph[j][z] == 'P') {
                        if(!bfs(j,z,graph,new boolean[5][5])) {
                            answer[i] = 0;
                            break;
                        }
                    }
                }
                if(answer[i] == 0) {
                    break;
                }
            }
        }
        return answer;
    }
    
    public char[][] createGraph(String[] place) {
        char[][] graph = new char[5][5];
        
        for(int i = 0; i < 5; i++) {
            for(int j = 0; j < 5; j++) {
                graph[i][j] = place[i].charAt(j);
            }
        }
        return graph;
    }
    
    public boolean bfs(int startR, int startC, char[][] graph, boolean[][] visited) {
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{startR,startC,0});
        visited[startR][startC] = true;
        
        int[] drs = {-1,1,0,0};
        int[] dcs = {0,0,-1,1};
        
        while(!queue.isEmpty()) {
            int[] cur = queue.poll();
            int r = cur[0];
            int c = cur[1];
            int distance = cur[2];
            
            for(int i = 0; i < 4; i++) {
                int nr = r + drs[i];
                int nc = c + dcs[i];
                
                if(0<= nr && nr < 5 && 0<= nc && nc < 5 && !visited[nr][nc] && graph[nr][nc] != 'X') {
                    if(graph[nr][nc] == 'P') {
                        if(distance + 1 <= 2) {
                            return false;
                        }
                    }
                    queue.add(new int[]{nr,nc,distance+1});
                    visited[nr][nc] = true;
                }
            }
        }
        return true;
    }
}