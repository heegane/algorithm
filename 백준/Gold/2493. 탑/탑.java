import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());

        // {height, index}
        Stack<int[]> stack = new Stack<>();
        int[] result = new int[n];

        String input = br.readLine();
        StringTokenizer st = new StringTokenizer(input);
        for (int i = 0; i < n; i++) {
            int height = Integer.parseInt(st.nextToken());
            while (!stack.isEmpty() && stack.peek()[0] <= height) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                result[i] = stack.peek()[1] + 1; // 송신탑의 인덱스를 결과 배열에 저장
            } else {
                result[i] = 0;
            }
            stack.push(new int[]{height, i});
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(result[i]).append(" ");
        }

        bw.write(sb.toString());
        br.close();
        bw.close();
    }
}
