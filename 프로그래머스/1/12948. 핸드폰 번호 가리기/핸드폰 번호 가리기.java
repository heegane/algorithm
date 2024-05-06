class Solution {
    public String solution(String phone_number) {
        String answer = "";
        int cnt = phone_number.length() - 4;
        for(int i = 0; i < cnt; i ++) {
            answer += '*';
        }
        
        for(int i = cnt; i < cnt + 4; i ++) {
            answer += phone_number.charAt(i);
        }
        return answer;
    }
}