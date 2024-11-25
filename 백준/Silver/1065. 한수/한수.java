import java.io.*;

public class Main {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int n = Integer.parseInt(br.readLine());
    int answer = 0;

    if (n < 100) {
      answer = n;
    } else {
      answer = 99;
      for (int i = 100; i <= n; i++) {
        int hun = i / 100;
        int ten = (i % 100) / 10;
        int one = i % 10;
        if ((hun - ten) == (ten - one)) {
          answer++;
        }
      }
    }

    bw.write(answer + "\n");
    bw.flush();
    bw.close();
    br.close();
  }
}
