package Java;
import java.util.Arrays;
import java.util.Scanner;

public class Problem5597 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        Boolean[] task = new Boolean[31];
        Arrays.fill(task, false);

        int num;
        for (int i = 0; i < 28; i++) {
            num = sc.nextInt();
            task[num] = true;
        }

        int count = 0;
        for (int i = 1; i < 31; i++) {
            if (!task[i] && count < 2) {
                count += 1;
                System.out.println(i);
            } else if (count == 2) {
                break;
            }
        }
        sc.close();
    }
}
