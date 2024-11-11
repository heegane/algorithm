import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, Integer> map = new HashMap<>();
        for(String[] cloth : clothes) {
            String name = cloth[0];
            String type = cloth[1];
            if(map.containsKey(type)) {
                map.put(type, map.get(type) + 1);
            } else {
                map.put(type, 1);
            }
        }
        for(Map.Entry<String, Integer> entrySet : map.entrySet()) {
            answer *= (entrySet.getValue() + 1);
        }
        answer--;
        return answer;
    }
}