package Java;

import java.io.*;
import java.util.*;

public class Problem10798 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arr = new String[5];
        int[] count = new int[5];
        int max_count = 0;
        for (int i = 0; i < 5; i++) {
            arr[i] = br.readLine();
            count[i] = arr[i].length();
            max_count = max_count < count[i] ? count[i] : max_count;
        }
        
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int idx = 0;
        while (true) {
            if (max_count == idx) {
                break;
            }
            for (int i = 0; i < 5; i++) {
                if (idx < count[i]) {
                    bw.write(arr[i].charAt(idx));
                }
            }
            idx++;
        }
        br.close();
        bw.flush();
        bw.close();
    }
    
}
