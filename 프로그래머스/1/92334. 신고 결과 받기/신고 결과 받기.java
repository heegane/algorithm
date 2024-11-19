import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int n = id_list.length;
        int[] answer = new int[n];
        Map<String, List<String>> reportMap = new HashMap<>();
        Map<String, Integer> cntMap = new HashMap<>();
        
        for(String r : report) {
            String[] data = r.split(" ");
            String from = data[0];
            String to = data[1];
            
            if(!reportMap.containsKey(from)) {
                reportMap.put(from, new ArrayList<>());
                reportMap.get(from).add(to);
            } else {
                if(reportMap.get(from).contains(to)) {
                    continue;
                } else {
                    reportMap.get(from).add(to);
                }
            }
            
            cntMap.put(to, cntMap.getOrDefault(to, 0) + 1);
        }
        
        for(int i = 0; i < n; i++) {
            String from = id_list[i];
            int cnt = 0;
            if(!reportMap.containsKey(from)) continue;
            
            for(String to : reportMap.get(from)) {
                if(cntMap.get(to) >= k) {
                    cnt++;
                }
            }
            answer[i] = cnt;
        }
        return answer;
    }
}