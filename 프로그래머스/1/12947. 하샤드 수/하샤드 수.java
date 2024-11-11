class Solution {
    public boolean solution(int x) {
        String num = Integer.toString(x);
        int n = 0;
        for(int i = 0; i < num.length(); i++) {
            n += num.charAt(i) - '0';
        }
        if(x % n == 0) {
            return true;
        } else {
            return false;
        }
    }
}