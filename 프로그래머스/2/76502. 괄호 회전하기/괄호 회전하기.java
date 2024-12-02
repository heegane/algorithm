import java.util.*;

class Solution {
    int answer;
    Map<Character, Character> map;
    public int solution(String s) {
        answer = 0;
        map = new HashMap<>();
        map.put(']', '[');
        map.put(')', '(');
        map.put('}', '{');
        Queue<Character> queue = new ArrayDeque<>();
        for(int i = 0; i < s.length(); i++) {
            queue.add(s.charAt(i));
        }
        
        for(int x = 0; x < s.length(); x++) {
            if(isValid(new ArrayDeque<>(queue))) {
                answer++;
            }
            queue.add(queue.poll());
        }
        return answer;
    }
    
    public boolean isValid(Queue<Character> queue) {
        Deque<Character> stack = new ArrayDeque<>();
        while(!queue.isEmpty()) {
            char element = queue.poll();
            if(stack.isEmpty()) {
                stack.push(element);
                continue;
            }
            
            if(map.containsKey(element) && stack.peek() == map.get(element)) {
                stack.pop();
            } else {
                stack.push(element);
            }
        }
        
        if(stack.isEmpty()) {
            return true;
        }
        return false;
    }
}