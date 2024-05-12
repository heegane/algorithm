class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int sum = brown + yellow;
        int j = 0, r = 0, c = 0;
        
        for(int i = 3; i <= sum; i ++) {
            if(sum%i == 0) {
                j = sum / i;
            } else {
                continue;
            }
            r = Math.max(i,j);
            c = Math.min(i,j);
            
            if((r-2) * (c-2) == yellow) {
                answer[0] = r;
                answer[1] = c;
                return answer;
            }
        }
        return answer;
    }
}