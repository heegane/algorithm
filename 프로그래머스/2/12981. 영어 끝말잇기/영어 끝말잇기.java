import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        Map<String, Boolean> map = new HashMap<>();
        char pre = words[0].charAt(words[0].length() - 1);
        map.put(words[0], true);

        for(int i = 1; i < words.length; i++) {
            String word = words[i];
            if(pre != word.charAt(0)) {
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                return answer;
            }
            if(map.containsKey(word)) {
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                return answer;
            } else {
                map.put(word, true);
            }
            pre = word.charAt(word.length() - 1);
        }

        return answer;
    }
}