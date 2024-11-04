import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        List<String[]> commands = new ArrayList<>();
        Map<String, String> map = new HashMap<>();
        
        for(String r : record) {
            String[] datas = r.split(" ");
            
            if(datas[0].equals("Enter")) {
                map.put(datas[1], datas[2]);
                commands.add(new String[]{datas[0], datas[1]});
            } else if(datas[0].equals("Leave")) {
                commands.add(new String[]{datas[0], datas[1]});
            } else {
                map.put(datas[1], datas[2]);
            }
        }
        
        String[] answer = new String[commands.size()];
        
        for(int i = 0; i < commands.size(); i++) {
            String[] command = commands.get(i);
            String name = map.get(command[1]);
            if(command[0].equals("Enter")) {
                answer[i] = name + "님이 들어왔습니다.";
            } else {
                answer[i] = name + "님이 나갔습니다.";
            }
        }
        
        return answer;
    }
}