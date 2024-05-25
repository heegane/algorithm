import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        int time = 0;
        Map<String,Integer> map = new HashMap<String,Integer>();
        
        if(cacheSize == 0) {
            answer = cities.length * 5;
            return answer;
        }
        
        for(String city:cities) {
            city = city.toUpperCase();
            time += 1;
            
            if(map.containsKey(city)) {
                answer += 1;
            } 
            else {
                if(map.size() == cacheSize) {
                    String findKey = "null";
                    
                    for(Map.Entry<String, Integer> entry : map.entrySet()) {
                        if(!map.containsKey(findKey)) {
                            findKey = entry.getKey();
                            continue;
                        }
                        
                        if(map.get(findKey) > entry.getValue()) {
                            findKey = entry.getKey();
                        }
                    }
                    map.remove(findKey);
                }
                answer += 5;
            }
            map.put(city, time);
        }
        return answer;
    }
}