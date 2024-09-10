import java.util.*;

public class Solution {
    public int solution(int n) {
        int ans = 0;
        int cur = n;
        if(n==1) return 1;
        if(n==2) return 1;
        
        while(true) {
            if(cur == 1) {
                ans += 1;
                break;
            }
            if(cur % 2 != 0) {
                ans += 1;
            }
            cur = cur / 2;
        }
        
        return ans;
    }
}