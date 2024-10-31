class Solution {
    int answer;
    int n;
    boolean[] visited;
    public int solution(int k, int[][] dungeons) {
        answer = 0;
        n = dungeons.length;
        visited = new boolean[n];
        dfs(k, dungeons, 0);
        return answer;
    }
    
    public void dfs(int k, int[][] dungeons, int cnt) {
        for(int i = 0; i < n; i++) {
            int[] dungeon = dungeons[i];
            if(dungeon[0] <= k && !visited[i]) {
                visited[i] = true;
                dfs(k-dungeon[1], dungeons, cnt + 1);
                visited[i] = false;
            }
        }
        answer = Math.max(answer, cnt);
    }
}