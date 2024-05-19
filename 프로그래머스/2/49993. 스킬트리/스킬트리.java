import java.util.*;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        int index = 0;
        boolean flag = true;
        HashMap<Character,Integer> hm = new HashMap<Character,Integer>();
        
        for(int i = 0; i < skill.length(); i++) {
            hm.put(skill.charAt(i),i);
        }
        
        for(String s : skill_trees) {
            for(int i = 0; i < s.length(); i++) {
                if(!hm.containsKey(s.charAt(i))) {
                    continue;
                }
                if(hm.get(s.charAt(i)) <= index) {
                    index += 1;
                } else {
                    flag = false;
                    break;
                }
            }
            if(flag) {
                answer += 1;
            }
            flag = true;
            index = 0;
        }
        
        return answer;
    }
}