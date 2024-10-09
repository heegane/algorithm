import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        List<Integer> answer = new ArrayList<>();
        int[] person1 = {1,2,3,4,5};
        int[] person2 = {2,1,2,3,2,4,2,5};
        int[] person3 = {3,3,1,1,2,2,4,4,5,5};
        int idx1 = 0;
        int idx2 = 0;
        int idx3 = 0;
        int score1 = 0;
        int score2 = 0;
        int score3 = 0;
        
        for(int i = 0; i < answers.length; i++) {
            if(person1[idx1 % person1.length] == answers[i]) {
                score1++;
            } 
            if(person2[idx2 % person2.length] == answers[i]) {
                score2++;
            } 
            if(person3[idx3 % person3.length] == answers[i]) {
                score3++;
            }
            idx1++;
            idx2++;
            idx3++;
        }
        
        int maxScore = Math.max(score1, Math.max(score2, score3));
        if(maxScore == score1) {
            answer.add(1);
        }
        if(maxScore == score2) {
            answer.add(2);
        }
        if(maxScore == score3) {
            answer.add(3);
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}