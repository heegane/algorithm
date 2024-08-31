import java.util.*;

class Solution {
    Set<Integer> candidates;
    public int solution(String numbers) {
        int size = numbers.length();
        candidates = new HashSet<>();
        int answer = 0;
        for(int i = 1; i <= size; i++) {
            dfs(i, numbers, new boolean[size], "");
        }
        
        for(int num:candidates) {
            if(isPrime(num)) answer++;
        }
        
        return answer;
    }
    
    
    public void dfs(int len, String numbers, boolean[] visited, String temp) {
        if(temp.length() == len) {
            candidates.add(Integer.parseInt(temp));
            return;
        }
        for(int i = 0; i < numbers.length(); i++) {
            if(!visited[i]) {
                visited[i] = true;
                dfs(len, numbers, visited, temp + numbers.charAt(i));
                visited[i] = false;
            }
        }
    }
    
    public boolean isPrime(int num) {
        if(num <= 1) return false;
        for(int i = 2; i * i <= num; i++) {
            if(num % i == 0) {
                return false;
            }
        }
        return true;
    }
}