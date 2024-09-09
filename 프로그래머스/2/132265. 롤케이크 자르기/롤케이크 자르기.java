import java.util.*;

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        Set<Integer> left = new HashSet<>();
        Map<Integer, Integer> right = new HashMap<>();
        
        for(int i = 0; i < topping.length; i++) {
            if(right.containsKey(topping[i])) {
                right.put(topping[i], right.get(topping[i])+1);
            } else {
                right.put(topping[i], 1);
            }
        }
        
        Deque<Integer> deque = new ArrayDeque<>();

        for (int t : topping) {
            deque.add(t);
        }
        
        while(deque.size() != 1) {
            int value = deque.poll();
            left.add(value);
            right.put(value, right.get(value) - 1);
            if(right.get(value) == 0) {
                right.remove(value);
            }
            if(left.size() == right.size()) {
                answer++;
            }
        }
        
        return answer;
    }
}