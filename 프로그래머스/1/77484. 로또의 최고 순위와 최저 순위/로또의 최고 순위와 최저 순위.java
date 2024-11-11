import java.util.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int highScore = 0;
        int lowScore = 0;
        int zeroCnt = 0;
        Map<Integer, Boolean> map = new HashMap<>();
        Map<Integer, Integer> score = new HashMap<>();
        
        for(int i = 6; i >= 2; i--) {
            score.put(i, 7-i);
        }
        
        for(int lotto : lottos) {
            if(lotto == 0) {
                zeroCnt++;
            } else {
                map.put(lotto, true);
            }
        }
        
        for(int win_num : win_nums) {
            if(map.containsKey(win_num)) {
                highScore++;
                lowScore++;
            }
        }
        highScore += zeroCnt;
        
        if(score.containsKey(highScore)) {
            answer[0] = score.get(highScore);
        } else {
            answer[0] = 6;
        }
        
        if(score.containsKey(lowScore)) {
            answer[1] = score.get(lowScore);
        } else {
            answer[1] = 6;
            
        }
        return answer;
    }
}