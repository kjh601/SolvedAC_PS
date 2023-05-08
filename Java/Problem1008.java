package Java;

import java.util.Scanner;

public class Problem1008 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        double A = sc.nextDouble();
        double B = sc.nextDouble();

        System.out.printf("%.10f", (A / B));

        sc.close();
    }
}
