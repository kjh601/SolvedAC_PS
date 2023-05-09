package Java;

import java.util.Scanner;

public class Problem2884 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int H = sc.nextInt();
        int M = sc.nextInt();
        
        M -= 45;
        if (M < 0) {
            H -= 1;
            if (H < 0) {
                H += 24;
            }
            M += 60;
        }
        System.out.println(H+" "+M);
        sc.close();
    }
}
