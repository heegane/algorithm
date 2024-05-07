import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        HashMap<Integer,Integer> ht = new HashMap<>();
        for(int num:numbers){
            if(!ht.containsKey(num)) {
                ht.put(num,1);
            }
        }
        for(int i=0; i<10; i++){
            if(!ht.containsKey(i)){
                answer += i;
            }
        }
        return answer;
    }
}