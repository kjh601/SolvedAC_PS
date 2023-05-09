package Java;

import java.util.Scanner;

public class Problem25304 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int X = sc.nextInt();
        int N = sc.nextInt();

        int a, b;

        int sum = 0;
        for (int i = 0; i < N; i++) {
            a = sc.nextInt();
            b = sc.nextInt();
            sum += a * b;
        }
        if (X == sum) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
        sc.close();
    }
}
