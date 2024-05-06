class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int cnt_p = 0;
        int cnt_y = 0;
        
        char[] charArray = s.toCharArray();
        
        for(int i = 0; i<s.length(); i++) {
            if (charArray[i] == 'p' || charArray[i] == 'P') {
                cnt_p += 1;
            } else if(charArray[i] == 'y' || charArray[i] == 'Y') {
                cnt_y += 1;
            }
        }
        
        if(cnt_p != cnt_y) {
            answer = false;
        }
        
        return answer;
    }
}