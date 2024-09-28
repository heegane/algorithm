import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        Deque<Integer> queue = new ArrayDeque<>();
        for(int i = 0; i < progresses.length; i++) {
            int progress = progresses[i];
            int speed = speeds[i];
            for(int j = 1; ; j++) {
                if(speed * j + progress >= 100) {
                    queue.add(j);
                    break;
                }
            }
        }
        
        int pre = queue.poll();
        int cnt = 1;
        while(!queue.isEmpty()) {
            if(pre < queue.peekFirst()) {
                answer.add(cnt);
                cnt = 1;
                pre = queue.poll();
            } else {
                cnt += 1;
                queue.poll();
            }
        }
        
        answer.add(cnt);
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}