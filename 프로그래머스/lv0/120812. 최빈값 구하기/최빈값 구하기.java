import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[] array) {
        int[] numbers = new int[1001];
        for (int i = 0; i < array.length; i++) {
            numbers[array[i]] += 1;
        }
                
        int max = 0;
        int idx = 0;
        for (int i = 0; i <= 1000; i++) {
            if (max < numbers[i]) {
                max = numbers[i];
                idx = i;
            }
        }
        
        int cnt = 0;
        for (int i = 0; i <= 1000; i++) {
            if (cnt > 1) {
                break;
            } else if (numbers[i] == max) {
                cnt += 1;
            }
        }
        
        int answer = 0;
        if (cnt > 1) {
            answer = -1;
        } else {
            answer = idx;
        }
        
        return answer;
    }
}