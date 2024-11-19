import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        StringBuilder answer = new StringBuilder();
        String[] nums = new String[numbers.length];
        
        for(int i = 0; i < numbers.length; i++) {
            nums[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(nums, (o1, o2) -> (o2 + o1).compareTo(o1 + o2));
        
        if(nums[0].equals("0")) {
            return "0";
        }
        
        for(int i = 0; i < numbers.length; i++) {
            answer.append(nums[i]);
        }
        
        return answer.toString();
    }
}