class Solution {
    int answer;
    int cnt;
    
    public int solution(String word) {
        answer = 0;
        cnt = 0;
        recursive(word, "");
        return answer;
    }
    
    public void recursive(String word, String temp) {
        
        if(temp.equals(word)) {
            answer = cnt;
            return;
        }
        
        cnt++;
        
        if(temp.length() == 5) {
            return;
        }
        
        recursive(word, temp + "A");
        recursive(word, temp + "E");
        recursive(word, temp + "I");
        recursive(word, temp + "O");
        recursive(word, temp + "U");
    }
}