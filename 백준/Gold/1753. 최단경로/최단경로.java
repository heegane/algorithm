import java.util.*;
import java.io.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    String[] input = br.readLine().split(" ");
    int v = Integer.parseInt(input[0]);
    int e = Integer.parseInt(input[1]);
    int start = Integer.parseInt(br.readLine());

    Map<Integer, List<Edge>> map = new HashMap<>();
    for (int i = 1; i <= v; i++) {
      map.put(i, new ArrayList<>());
    }

    for (int i = 0; i < e; i++) {
      String[] data = br.readLine().split(" ");
      map.get(Integer.parseInt(data[0]))
        .add(new Edge(Integer.parseInt(data[1]), Integer.parseInt(data[2])));
    }

    Queue<Edge> queue = new PriorityQueue<>();
    queue.add(new Edge(start, 0));
    int[] costs = new int[v + 1];
    Arrays.fill(costs, Integer.MAX_VALUE);
    costs[start] = 0;

    while (!queue.isEmpty()) {
      Edge cur = queue.poll();

      if (cur.cost > costs[cur.node]) {
        continue;
      }

      for (Edge next : map.get(cur.node)) {
        int nextCost = cur.cost + next.cost;
        if (nextCost < costs[next.node]) {
          costs[next.node] = nextCost;
          queue.add(new Edge(next.node, nextCost));
        }
      }
    }

    for (int i = 1; i <= v; i++) {
      if (costs[i] == Integer.MAX_VALUE) {
        bw.write("INF" + "\n");
      } else {
        bw.write(costs[i] + "\n");
      }
    }
    bw.flush();
    bw.close();
    br.close();
  }

  public static class Edge implements Comparable<Edge> {

    int node;
    int cost;

    public Edge(int node, int cost) {
      this.node = node;
      this.cost = cost;
    }

    @Override
    public int compareTo(Edge other) {
      return Integer.compare(this.cost, other.cost);
    }
  }
}
