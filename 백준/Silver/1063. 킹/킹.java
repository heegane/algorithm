import java.io.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    String[] input = br.readLine().split(" ");
    int[] king = new int[]{8 - (input[0].charAt(1) - '0'), input[0].charAt(0) - 65};
    int[] stone = new int[]{8 - (input[1].charAt(1) - '0'), input[1].charAt(0) - 65};
    int n = Integer.parseInt(input[2]);

    int[] drs = {0, 0, 1, -1, -1, -1, 1, 1};
    int[] dcs = {1, -1, 0, 0, 1, -1, 1, -1};

    for (int i = 0; i < n; i++) {
      String command = br.readLine();
      int nextIdx;

      if (command.equals("R")) {
        nextIdx = 0;
      } else if (command.equals("L")) {
        nextIdx = 1;
      } else if (command.equals("B")) {
        nextIdx = 2;
      } else if (command.equals("T")) {
        nextIdx = 3;
      } else if (command.equals("RT")) {
        nextIdx = 4;
      } else if (command.equals("LT")) {
        nextIdx = 5;
      } else if (command.equals("RB")) {
        nextIdx = 6;
      } else {
        nextIdx = 7;
      }

      int[] nextKing = {king[0] + drs[nextIdx], king[1] + dcs[nextIdx]};

      // 킹 밖으로 나갈 경우
      if (nextKing[0] < 0 || nextKing[0] >= 8 || nextKing[1] < 0 || nextKing[1] >= 8) {
        continue;
      }

      if (nextKing[0] == stone[0] && nextKing[1] == stone[1]) {
        if (stone[0] + drs[nextIdx] < 0 || stone[0] + drs[nextIdx] >= 8
          || stone[1] + dcs[nextIdx] < 0 || stone[1] + dcs[nextIdx] >= 8) {
          continue;
        } else {
          stone[0] += drs[nextIdx];
          stone[1] += dcs[nextIdx];
        }
      }
      king[0] = nextKing[0];
      king[1] = nextKing[1];

    }

    String finalKing = (char) (65 + king[1]) + String.valueOf(8 - king[0]);
    String finalStone = (char) (65 + stone[1]) + String.valueOf(8 - stone[0]);

    bw.write(finalKing + "\n" + finalStone + "\n");
    bw.flush();
    bw.close();
    br.close();
  }
}
