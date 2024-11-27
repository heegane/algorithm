import java.io.*;
import java.util.StringTokenizer;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int answer = 0;
    StringTokenizer st = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(st.nextToken());
    int m = Integer.parseInt(st.nextToken());
    int[][] map = new int[n][m];
    st = new StringTokenizer(br.readLine());
    int r = Integer.parseInt(st.nextToken());
    int c = Integer.parseInt(st.nextToken());
    int d = Integer.parseInt(st.nextToken());

    for (int i = 0; i < n; i++) {
      String[] data = br.readLine().split(" ");
      for (int j = 0; j < m; j++) {
        map[i][j] = Integer.parseInt(data[j]);
      }
    }

    // 북동남서
    int[] drs = {-1, 0, 1, 0};
    int[] dcs = {0, 1, 0, -1};

    while (true) {
      // 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소
      if (isBlank(map, r, c)) {
        map[r][c] = 2; // 청소
        answer++;
      }

      // 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
      if (!isNearByBlank(map, r, c, drs, dcs)) {
        int idx = (d + 2) % 4; // 후진
        int nextR = r + drs[idx];
        int nextC = c + dcs[idx];

        // 뒤쪽 칸이 벽이라 후진할 수 없다면 작동 멈춤
        if (map[nextR][nextC] == 1) {
          break;
        }
        // 한 칸 후진
        else {
          r = nextR;
          c = nextC;
        }
      }
      // 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
      else {
        // 반시계 방향으로 90도 회전
        d--;
        if (d == -1) {
          d = 3;
        }
        int nextR = r + drs[d];
        int nextC = c + dcs[d];

        // 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
        if (map[nextR][nextC] == 0) {
          r = nextR;
          c = nextC;
        }
      }
    }

    bw.write(String.valueOf(answer));
    bw.flush();
    bw.close();
    br.close();
  }

  public static boolean isBlank(int[][] map, int r, int c) {
    if (map[r][c] == 0) {
      return true;
    }
    return false;
  }

  public static boolean isNearByBlank(int[][] map, int r, int c, int[] drs, int[] dcs) {
    for (int i = 0; i < 4; i++) {
      int nextR = r + drs[i];
      int nextC = c + dcs[i];
      if (map[nextR][nextC] == 0) {
        return true;
      }
    }
    return false;
  }
}
