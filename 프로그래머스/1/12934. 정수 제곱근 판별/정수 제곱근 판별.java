class Solution {
    public long solution(long n) {
        long answer = 1;
        while(answer <= n) {
            if(answer * answer == n) {
                answer = (answer+1) * (answer+1);
                return answer;
            } else {
                answer += 1;
            }
        }
        return -1;
    }
}