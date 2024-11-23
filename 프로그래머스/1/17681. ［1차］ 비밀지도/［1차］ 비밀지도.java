import java.util.*;

class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        int[][] graph1 = new int[n][n];
        int[][] graph2 = new int[n][n];
        makeGraph(graph1, arr1, n);
        makeGraph(graph2, arr2, n);
        
        for(int i = 0; i < n; i++) {
            StringBuilder result = new StringBuilder();
            for(int j = 0; j < n; j++) {
                if(graph1[i][j] == 1 || graph2[i][j] == 1) {
                    result.append("#");
                } else {
                    result.append(" ");
                }
            }
            answer[i] = result.toString();
        }
        return answer;
    }
    
    public void makeGraph(int[][] graph, int[] arr, int n) {
        for (int i = 0; i < arr.length; i++) {
            String binary = String.format("%" + n + "s", Integer.toBinaryString(arr[i])).replace(' ', '0');
            for (int j = 0; j < n; j++) {
                graph[i][j] = binary.charAt(j) - '0'; // 각 문자 -> 숫자로 변환
            }
        }
    }
}