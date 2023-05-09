package Java;

import java.util.Scanner;

public class Problem8393 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        
        System.out.println(n * (1 + n) / 2);
        
        sc.close();
    }
    
}
