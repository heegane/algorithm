class Solution {
    int answer;
    int n;
    public int solution(int[] numbers, int target) {
        answer = 0;
        n = numbers.length;
        dfs(0, numbers, target, 0);
        return answer;
    }
    
    public void dfs(int start, int[] numbers, int target, int num) {
        if(start == n) {
            if(num == target) {
                answer++;
            }
            return;
        }
        dfs(start + 1, numbers, target, num + numbers[start]);
        dfs(start + 1, numbers, target, num - numbers[start]);
    }
}