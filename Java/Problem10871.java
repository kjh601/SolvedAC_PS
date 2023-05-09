package Java;

import java.util.Scanner;

public class Problem10871 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int X = sc.nextInt();

        int num;
        for (int i = 0; i < N; i++) {
            num = sc.nextInt();

            if (num < X) {
                System.out.println(num);
            }
        }
        sc.close();
    }
}
