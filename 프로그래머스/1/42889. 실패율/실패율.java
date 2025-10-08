import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        int total = stages.length; 

        List<Stage> list = new ArrayList<>();

        for (int i = 1; i <= N; i++) {
            int fail = 0;

            for (int s : stages) {
                if (s == i) fail++;
            }

            double rate = 0;
            if (total != 0) {
                rate = (double) fail / total;
            }

            list.add(new Stage(i, rate));
            total -= fail; 
        }

        Collections.sort(list, (a, b) -> {
            if (b.rate == a.rate)
                return a.num - b.num;
            else
                return Double.compare(b.rate, a.rate);
        });

        for (int i = 0; i < N; i++) {
            answer[i] = list.get(i).num;
        }

        return answer;
    }
}


class Stage {
    int num;
    double rate;

    Stage(int num, double rate) {
        this.num = num;
        this.rate = rate;
    }
}
