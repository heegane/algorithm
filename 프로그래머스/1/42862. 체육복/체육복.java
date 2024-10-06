import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n - lost.length;
        Arrays.sort(lost);
        Arrays.sort(reserve);
        
        // 도난당한 학생이 여벌의 체육복이 있는 경우
        for(int i = 0; i < lost.length; i++) {
            for(int j = 0; j < reserve.length; j++) {
                if(lost[i] == reserve[j]) {
                    answer++;
                    lost[i] = -1;
                    reserve[j] = -1;
                }
            }
        }
        
        // 빌려주는 경우
        for(int i = 0; i < lost.length; i++) {
            if(lost[i] == -1) continue;
            
            for(int j = 0; j < reserve.length; j++) {
                if(reserve[j] != -1 && Math.abs(lost[i] - reserve[j]) == 1) {
                    answer++;
                    reserve[j] = -1;
                    break;
                }
            }
        }
        
        
        return answer;
    }
}