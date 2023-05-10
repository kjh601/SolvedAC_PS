package Java;

import java.io.*;
import java.util.StringTokenizer;

public class Problem2563 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        boolean[][] board = new boolean[100][100];
        StringTokenizer st;
        int X, Y;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            X = Integer.parseInt(st.nextToken())-1;
            Y = Integer.parseInt(st.nextToken())-1;
            for (int x = X; x < X+10; x++) {
                for (int y = Y; y < Y+10; y++) {
                    board[x][y] = true;
                }
            }
        }

        int count = 0;
        for (int i = 0; i < 100; i++) {
            for (int j = 0; j < 100; j++) {
                if(board[i][j]){
                    count += 1;
                }
            }
        }

        System.out.println(count);
        br.close();
    }
}
