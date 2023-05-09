package Java;

import java.io.*;
import java.util.StringTokenizer;

public class Problem10818 {
    public static void main(String[] args) throws IOException {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int min = 1000000;
        int max = -1000000;
        int num;
        for (int i = 0; i < N; i++) {
            num = Integer.parseInt(st.nextToken());
            min = Math.min(num, min);
            max = Math.max(num, max);
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(min + " " + max);
        bw.flush();
        br.close();
    }
}
