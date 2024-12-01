import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int n = Integer.parseInt(br.readLine());
    Map<Integer, List<Integer>> map = new HashMap<>();
    for (int i = 1; i <= n; i++) {
      map.put(i, new ArrayList<>());
    }

    // 연결 리스트
    for (int i = 0; i < n - 1; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      int a = Integer.parseInt(st.nextToken());
      int b = Integer.parseInt(st.nextToken());
      map.get(a).add(b);
      map.get(b).add(a);
    }

    // {1=[6, 4], 2=[4], 3=[6, 5], 4=[1, 2, 7], 5=[3], 6=[1, 3], 7=[4]}
    boolean[] visited = new boolean[n + 1];
    int[] parent = new int[n + 1];
    Queue<Integer> queue = new ArrayDeque<>();
    queue.add(1); // 트리의 루트를 1로 설정
    while (!queue.isEmpty()) {
      int p = queue.poll();
      for (int v : map.get(p)) {
        if (!visited[v]) {
          queue.add(v);
          visited[v] = true;
          parent[v] = p;
        }
      }
    }

    for (int i = 2; i <= n; i++) {
      bw.write(parent[i] + "\n");
    }
    bw.flush();
    bw.close();
    br.close();
  }
}
