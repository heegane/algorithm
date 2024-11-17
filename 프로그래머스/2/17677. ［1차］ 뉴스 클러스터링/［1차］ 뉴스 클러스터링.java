import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();

        // 다중집합들 생성
        Map<String, Integer> map1 = createMultiset(str1);
        Map<String, Integer> map2 = createMultiset(str2);

        // 교집합과 합집합 크기 계산
        int intersection = 0;
        int union = 0;

        Set<String> allKeys = new HashSet<>(map1.keySet());
        allKeys.addAll(map2.keySet());

        for (String key : allKeys) {
            int count1 = map1.getOrDefault(key, 0);
            int count2 = map2.getOrDefault(key, 0);

            intersection += Math.min(count1, count2);
            union += Math.max(count1, count2);
        }

        if (union == 0) {
            return 65536; // 두 다중집합이 모두 공집합인 경우
        }

        // 자카드 유사도 계산 및 정수형으로 변환
        return (int)(((double) intersection / union) * 65536);
    }

    private Map<String, Integer> createMultiset(String str) {
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < str.length() - 1; i++) {
            String temp = str.substring(i, i + 2);
            if (temp.matches("[a-z]{2}")) {
                map.put(temp, map.getOrDefault(temp, 0) + 1);
            }
        }
        return map;
    }
}