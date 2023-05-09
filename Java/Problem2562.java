package Java;

import java.io.*;
import java.util.StringTokenizer;

public class Problem2562 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int num;

        int max_num = 0;
        int idx = -1;
        for (int i = 0; i < 9; i++) {
            st = new StringTokenizer(br.readLine());
            num = Integer.parseInt(st.nextToken());

            if (max_num < num) {
                max_num = num;
                idx = i;
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(max_num + "\n" + (idx+1));
        bw.flush();
        bw.close();
    }
}
