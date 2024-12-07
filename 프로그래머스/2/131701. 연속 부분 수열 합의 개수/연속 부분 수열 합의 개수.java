import java.util.*;

class Solution {
    Set<Integer> set;
    public int solution(int[] elements) {
        int answer = 0;
        set = new HashSet<>();
        
        // 길이가 1
        for(int element : elements) {
            set.add(element);
        }
        
        for(int i = 2; i < elements.length; i++) {
            getCandidates(elements, i);
        }
        
        // 길이가 elements.length
        int sum = 0;
        for(int element : elements) {
            sum += element;
        }
        set.add(sum);
        
        answer = set.size();
        return answer;
    }
    
    public void getCandidates(int[] elements, int len) {
        int n = elements.length;
        int left = 0;
        int right = left + len - 1;
        
        int sum = 0;
        for(int i = left; i <= right; i++) {
            sum += elements[i];
        }
        set.add(sum);
        
        int cnt = 1;
        while(cnt <= elements.length) {
            sum -= elements[left];
            right = right + 1 == n ? 0 : right + 1;
            sum += elements[right];
            left = left + 1 == n ? 0 : left + 1;
            set.add(sum);
            cnt++;
        }
    }
}