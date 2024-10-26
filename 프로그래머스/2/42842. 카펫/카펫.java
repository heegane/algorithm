class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        for(int w = 1; ; w++) {
            for(int h = 1; h <= w; h++) {
                if(2 * w + 2 * (h - 2) == brown && w * h - brown == yellow) {
                    answer[0] = w;
                    answer[1] = h;
                    return answer;
                }
            }
        }
    }
}