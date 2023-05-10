package Java;

import java.io.*;
import java.util.StringTokenizer;

public class Problem2566 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int max_num = 0;
        int num;
        int r = 1, c = 1;
        for (int i = 0; i < 9; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 9; j++) {
                num = Integer.parseInt(st.nextToken());
                if (max_num < num) {
                    max_num = num;
                    r = i;
                    c = j;
                }
            }
        }
        System.out.println(max_num + "\n" + (r + 1) + " " + (c + 1));
        br.close();
    }
}