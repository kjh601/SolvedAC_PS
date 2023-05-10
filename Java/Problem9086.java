package Java;

import java.io.*;

public class Problem9086 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        String str;
        for (int i = 0; i < T; i++) {
            str = br.readLine();
            bw.write(str.charAt(0) +""+ str.charAt(str.length() - 1)+"\n");
        }
        br.close();
        bw.flush();
        bw.close();
    }
}
