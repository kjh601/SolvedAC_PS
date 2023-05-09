package Java;

import java.util.Scanner;

public class Problem10869 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int A = sc.nextInt();
        int B = sc.nextInt();

        System.out.println((A + B)+ "\n" + (A - B) + "\n" + A * B + "\n" + A / B + '\n' + A % B);
        sc.close();
    }
}
