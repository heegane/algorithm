import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        
        Deque<Integer> stack = new ArrayDeque<>();
        for(int move : moves) {
            int i = move - 1;
            for(int j = 0; j < board.length; j++) {
                if(board[j][i] != 0) {
                    int toy = board[j][i];
                    board[j][i] = 0;
                    
                    if(!stack.isEmpty() && stack.peek() == toy) {
                        stack.pop();
                        answer += 2;
                    } else {
                        stack.push(toy);
                    }
                    break;
                }
            }
        }
        return answer;
    }
}