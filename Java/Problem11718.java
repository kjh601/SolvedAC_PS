package Java;

import java.io.*;
import java.util.StringTokenizer;

public class Problem11718{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        while (true) {
            String string = br.readLine();
            if (string == null)
                break;
            bw.write(string+'\n');
        }
        bw.flush();
        bw.close();
        br.close();
    }
}