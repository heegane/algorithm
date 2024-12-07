import java.util.*;

class Solution {
    // UDRL
    int[] dr = {-1, 1, 0, 0};
    int[] dc = {0, 0, 1, -1};

    public int solution(String dirs) {
        Set<String> visitedPaths = new HashSet<>();
        int[] cur = {0, 0};

        for (char dir : dirs.toCharArray()) {
            int nextR = cur[0];
            int nextC = cur[1];
            
            switch (dir) {
                case 'U':
                    nextR += dr[0];
                    nextC += dc[0];
                    break;
                case 'D':
                    nextR += dr[1];
                    nextC += dc[1];
                    break;
                case 'R':
                    nextR += dr[2];
                    nextC += dc[2];
                    break;
                case 'L':
                    nextR += dr[3];
                    nextC += dc[3];
                    break;
            }
            
            if (-5 <= nextR && nextR <= 5 && -5 <= nextC && nextC <= 5) {
                // 양방향 저장
                String path1 = cur[0] + "," + cur[1] + "-" + nextR + "," + nextC;
                String path2 = nextR + "," + nextC + "-" + cur[0] + "," + cur[1];
                
                visitedPaths.add(path1);
                visitedPaths.add(path2);
                
                cur[0] = nextR;
                cur[1] = nextC;
            }
        }

        return visitedPaths.size() / 2;
    }
}
