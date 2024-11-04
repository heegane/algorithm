import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Map<String, Boolean> map = new HashMap<>();
        for(String phone : phone_book) {
            map.put(phone, true);
        }
        
        for(String phone : phone_book) {
            String temp = "";
            for(int i = 0; i < phone.length() - 1; i++) {
                temp += phone.charAt(i);
                if(map.containsKey(temp)) {
                    return false;
                }
            }
        }
        return true;
    }
}