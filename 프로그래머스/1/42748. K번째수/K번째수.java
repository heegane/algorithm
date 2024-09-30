import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        int idx = 0;
        for(int[] command: commands) {
            int i = command[0];
            int j = command[1];
            int k = command[2];
            int[] temp = Arrays.copyOfRange(array, i - 1, j);
            Arrays.sort(temp);
            answer[idx] = temp[k - 1];
            idx++;
        }
        return answer;
    }
}