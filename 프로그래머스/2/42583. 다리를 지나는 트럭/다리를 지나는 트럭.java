import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int totalWeightOnBridge = 0;
        Queue<Integer> bridgeQueue = new LinkedList<>();
        Queue<Integer> timeQueue = new LinkedList<>();

        int i = 0;
        while (i < truck_weights.length || !bridgeQueue.isEmpty()) {
            answer++;
            
            if (!timeQueue.isEmpty() && timeQueue.peek() == answer) {
                timeQueue.poll();
                totalWeightOnBridge -= bridgeQueue.poll();
            }

            if (i < truck_weights.length && totalWeightOnBridge + truck_weights[i] <= weight) {
                bridgeQueue.add(truck_weights[i]);
                totalWeightOnBridge += truck_weights[i];
                timeQueue.add(answer + bridge_length);
                i++;
            }
        }

        return answer;
    }
}
