import java.util.*;
import java.io.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());

    int[][] graph = new int[n][m];
    for (int i = 0; i < n; i++) {
      String[] row = br.readLine().split(" ");
      for (int j = 0; j < m; j++) {
        graph[i][j] = Integer.parseInt(row[j]);
      }
    }

    int answer = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (graph[i][j] == 0) {
          answer = Math.max(answer, bfs(graph, new int[]{i, j}, n, m));
        }
      }
    }

    bw.write(answer + "\n");
    bw.flush();
    bw.close();
    br.close();
  }

  static int bfs(int[][] graph, int[] start, int n, int m) {
    boolean[][] visited = new boolean[n][m];
    visited[start[0]][start[1]] = true;
    Queue<int[]> queue = new ArrayDeque<>();
    queue.add(new int[]{start[0], start[1], 0});

    int[] drs = {-1, 1, 0, 0, -1, -1, 1, 1};
    int[] dcs = {0, 0, -1, 1, 1, -1, 1, -1};
    while (!queue.isEmpty()) {
      int[] cur = queue.poll();
      int r = cur[0];
      int c = cur[1];
      int d = cur[2];
      for (int i = 0; i < 8; i++) {
        int nextR = r + drs[i];
        int nextC = c + dcs[i];
        if (0 <= nextR && nextR < n && 0 <= nextC && nextC < m) {
          if (graph[nextR][nextC] == 0) {
            if (!visited[nextR][nextC]) {
              visited[nextR][nextC] = true;
              queue.add(new int[]{nextR, nextC, d + 1});
            }
          } else {
            return d + 1;
          }
        }
      }
    }
    return 0;
  }
}
