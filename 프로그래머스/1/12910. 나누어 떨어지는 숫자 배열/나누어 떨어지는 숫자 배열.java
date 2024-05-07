import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> arrayList = new ArrayList<Integer>();
        
        for(int v:arr) {
            if(v%divisor == 0) {
                arrayList.add(v);
            }
        }
        if(arrayList.size() == 0) {
            int[] answer = {-1};
            return answer;
        } else{
            Collections.sort(arrayList);
        }
        
        int[] answer = arrayList.stream().mapToInt(Integer::intValue).toArray();
        
        return answer;
    }
}