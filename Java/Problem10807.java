package Java;

import java.util.Scanner;

public class Problem10807 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        int v = sc.nextInt();
        int count = 0;
        for (int i = 0; i < N; i++) {
            if (arr[i] == v) {
                count += 1;
            }
        }
        System.out.println(count);

        sc.close();
    }
}
