import java.io.*;
import java.util.*;

public class Main {

  static int n;
  static int m;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    // 가로 길이 n, 세로 크기 m
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    char[][] graph = new char[m][n];
    for (int i = 0; i < m; i++) {
      String input = br.readLine();
      for (int j = 0; j < n; j++) {
        graph[i][j] = input.charAt(j);
      }
    }

    int cntW = 0;
    int cntB = 0;
    boolean[][] visited = new boolean[m][n];
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (!visited[i][j]) {
          int temp = bfs(graph, graph[i][j], i, j, visited);
          if (graph[i][j] == 'W') {
            cntW += temp * temp;
          } else {
            cntB += temp * temp;
          }
        }
      }
    }

    bw.write(cntW + " " + cntB);
    bw.flush();
    bw.close();
    br.close();
  }

  public static int bfs(char[][] graph, char type, int r, int c, boolean[][] visited) {
    Queue<int[]> queue = new ArrayDeque<>();
    visited[r][c] = true;
    queue.add(new int[]{r, c});
    int cnt = 1;
    int[] dr = {-1, 1, 0, 0};
    int[] dc = {0, 0, -1, 1};

    while (!queue.isEmpty()) {
      int[] cur = queue.poll();
      for (int i = 0; i < 4; i++) {
        int nr = cur[0] + dr[i];
        int nc = cur[1] + dc[i];
        if (0 <= nr && nr < m && 0 <= nc && nc < n && !visited[nr][nc] && graph[nr][nc] == type) {
          cnt++;
          queue.add(new int[]{nr, nc});
          visited[nr][nc] = true;
        }
      }
    }
    return cnt;
  }
}
