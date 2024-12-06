import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    Deque<int[]> stack = new ArrayDeque<>();
    int answer = 0;

    int n = Integer.parseInt(br.readLine());
    for (int i = 0; i < n; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int type = Integer.parseInt(st.nextToken());
      if (type == 0) {
        if (!stack.isEmpty()) {
          int[] top = stack.pop();
          if (top[1] == 1) {
            answer += top[0];
          } else {
            int remainder = top[1] - 1;
            stack.push(new int[]{top[0], remainder});
          }
        }
      } else {
        int a = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());
        if (t == 1) {
          answer += a;
        } else {
          stack.push(new int[]{a, t - 1});
        }
      }
    }

    bw.write(String.valueOf(answer));
    bw.flush();
    bw.close();
    br.close();
  }
}
