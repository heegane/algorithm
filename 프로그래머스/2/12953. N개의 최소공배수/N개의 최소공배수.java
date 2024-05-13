class Solution {
    public int solution(int[] arr) {
        int answer = arr[0];
        
        for(int i = 1; i < arr.length; i++) {
            if(Math.max(answer,arr[i]) % Math.min(answer,arr[i]) == 0) {
                answer = Math.max(answer,arr[i]);
            } else {
                int j = 2;
                while(true) {
                    int new_answer = Math.max(answer,arr[i]) * j;
                    if(new_answer % answer == 0 && new_answer % arr[i] == 0) {
                        answer = new_answer;
                        break;
                    } else{
                        j += 1;
                    }
                }
            }
        }
        return answer;
    }
}