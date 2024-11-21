import java.lang.reflect.Array;
import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    StringTokenizer st = new StringTokenizer(br.readLine());
    int m = Integer.parseInt(st.nextToken());
    int n = Integer.parseInt(st.nextToken());
    int k = Integer.parseInt(st.nextToken());

    int[][] graph = new int[m][n];
    for (int i = 0; i < k; i++) {
      st = new StringTokenizer(br.readLine());
      int startY = Integer.parseInt(st.nextToken());
      int startX = Integer.parseInt(st.nextToken());
      int endY = Integer.parseInt(st.nextToken());
      int endX = Integer.parseInt(st.nextToken());

      for (int x = startX; x < endX; x++) {
        for (int y = startY; y < endY; y++) {
          graph[x][y] = 1;
        }
      }
    }

    int[][] visited = new int[m][n];
    int cnt = 0;
    List<Integer> results = new ArrayList<>();
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (graph[i][j] == 0 && visited[i][j] == 0) {
          cnt++;
          results.add(bfs(new int[]{i, j}, visited, cnt, graph, m, n));
        }
      }
    }

    Collections.sort(results);
    bw.write(cnt + "\n");
    bw.write(results.stream()
      .map(String::valueOf)
      .collect(Collectors.joining(" "))
      + "\n");

    bw.flush();
    bw.close();
    br.close();
  }

  public static int bfs(int[] start, int[][] visited, int type, int[][] graph, int m, int n) {
    Queue<int[]> queue = new ArrayDeque<>();
    queue.add(start);
    visited[start[0]][start[1]] = type;

    int[] drs = {-1, 1, 0, 0};
    int[] dcs = {0, 0, -1, 1};

    while (!queue.isEmpty()) {
      int[] cur = queue.poll();
      int r = cur[0];
      int c = cur[1];
      for (int i = 0; i < 4; i++) {
        int nextR = r + drs[i];
        int nextC = c + dcs[i];
        if (0 <= nextR && nextR < m && 0 <= nextC && nextC < n && graph[nextR][nextC] == 0
          && visited[nextR][nextC] == 0) {
          visited[nextR][nextC] = type;
          queue.add(new int[]{nextR, nextC});

        }
      }
    }

    int result = 0;
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (visited[i][j] == type) {
          result++;
        }
      }
    }
    return result;
  }
}
