import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        
        PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
        
        for (int work : works) {
            q.offer(work);
        }
        
        for (int i = 0; i < n; i++) {
            if (q.isEmpty()) break;
            
            int temp = q.poll();
            if (temp <= 0) break;
            
            q.offer(temp - 1);
        }
        
        for (int remain : q) {
            answer += (long) remain * remain;
        }
        
        return answer;
    }
}
