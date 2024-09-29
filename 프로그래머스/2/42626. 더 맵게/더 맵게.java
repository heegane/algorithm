import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        Queue<Integer> pq = new PriorityQueue<>();
        for(int s : scoville) {
            pq.add(s);
        }
        while(pq.size() > 1) {
            if(pq.peek() >= K) {
                return answer;
            }
            int a = pq.poll();
            int b = pq.poll();
            pq.add(a + (b * 2));
            answer++;
        }
        if(pq.peek() >= K) {
            return answer;
        } else {
            return -1;
        }
    }
}