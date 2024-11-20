import java.util.*;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        
        for (int h = n; h >= 0; h--) {
            int count = 0;
            for (int citation : citations) {
                if (citation >= h) {
                    count++;
                }
            }
            if (count >= h) {
                return h; // H-Index 조건 만족 시 반환
            }
        }
        return 0;
    }
}