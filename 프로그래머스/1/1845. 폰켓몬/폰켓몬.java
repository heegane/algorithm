import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int n = nums.length/2;
        int answer = 0;
        
        Set<Integer> set = new HashSet<>();
        for(int num: nums) {
            set.add(num);
        }
        if(set.size() >= n) {
            answer = n;
        } else {
            answer = set.size();
        }

        return answer;
    }
}