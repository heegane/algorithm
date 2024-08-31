import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int totalTime = 0;
        int curTime = 0;
        int curIdx = 0;
        int cnt = 0;
        
        Arrays.sort(jobs, (j1,j2) -> j1[0] - j2[0]);
        Queue<int[]> pq = new PriorityQueue<>((o1,o2)->o1[1] - o2[1]);
        
        while(cnt < jobs.length) {
            while(curIdx < jobs.length && curTime >= jobs[curIdx][0]) {
                pq.add(jobs[curIdx]);
                curIdx++;
            }
            if(pq.isEmpty()){
                curTime = jobs[curIdx][0];
            } else {
                int[] job = pq.poll();
                totalTime += job[1] + curTime - job[0];
                curTime += job[1];
                cnt++;
            }
        }
        
        return totalTime/jobs.length;
    }
}