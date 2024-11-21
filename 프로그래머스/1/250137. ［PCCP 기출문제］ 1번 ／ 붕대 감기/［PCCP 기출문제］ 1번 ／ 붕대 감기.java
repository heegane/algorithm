import java.util.*;

class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int t = bandage[0]; // t초 동안
        int x = bandage[1]; // x만큼 회복
        int y = bandage[2];
        
        Map<Integer, Integer> map = new HashMap<>();
        for(int[] attack : attacks) {
            map.put(attack[0], attack[1]);
        }
        int n = attacks.length;
        int maxHealth = health;
        
        int cnt = 0;
        for(int i = 0; i <= attacks[n-1][0]; i++) {
            // 공격 들어올 때
            if(map.containsKey(i)) {
                cnt = 0; // 연속 성공 초기화
                health -= map.get(i);
                if(health <= 0) {
                    return -1;
                }
            }
            // 공격 안 들어올 때
            else {
                cnt++; // 연속 성공
                if(health + x > maxHealth) {
                    health = maxHealth;
                } else {
                    health += x;
                }
                
                if(cnt == t) {
                    if(health + y > maxHealth) {
                        health = maxHealth;
                    } else {
                        health += y;
                    }
                    cnt = 0; // 연속 성공 초기화
                }
            }
        }
        return health;
    }
}