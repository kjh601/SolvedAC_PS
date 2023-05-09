package Java;

import java.util.Scanner;

public class Problem9498 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int score = sc.nextInt();
        char grade;
        if (score > 89) {
            grade = 'A';
        } else if (score > 79) {
            grade = 'B';
        } else if (score > 69) {
            grade = 'C';
        } else if (score > 59) {
            grade = 'D';
        } else {
            grade = 'F';
        }

        System.out.println(grade);

        sc.close();
    }
}
