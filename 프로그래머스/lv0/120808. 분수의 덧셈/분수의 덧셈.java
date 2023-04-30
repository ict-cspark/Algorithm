class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int a = 0;
        int b = 0;
        a = (numer1 * denom2) + (numer2 * denom1);
        b = denom1 * denom2;
        
        int i = 2;
        while (i<=b) {
            if (a % i == 0 && b % i == 0) {
                a = a / i;
                b = b / i;
                i = 2;
            } else {
                i = i + 1;
            }
        }
        
        int[] answer = {a, b};
        return answer;
    }
}