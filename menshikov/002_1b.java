import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        b1();
    }

    static void b1() {
        int n = sc.nextInt();
        long sum = sc.nextInt();

        int[] arr = new int[n];
        char[] sign = new char[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            sign[i] = '-';
        }

        long cursum = arr[0];
        for (int i = 1; i < n; i++) cursum -= arr[i];

        int m = 0;

        while (sign[0] != '+') {
            if (cursum == sum) break;

            m++;
            int k = m;
            for (int i = n - 1; i >= 0; i--) {
                if ((k & 1) == 0 && sign[i] == '+') {
                    cursum -= (arr[i] * 2);
                    sign[i] = '-';
                } else if ((k & 1) == 1 && sign[i] == '-') {
                    cursum += (arr[i] * 2);
                    sign[i] = '+';
                }
                k >>= 1;
            }
        }

        if (cursum != sum) {
            System.out.println("No solution");
            return;
        }

        for (int i = 0; i < n; i++) {
            System.out.print(arr[i]);
            if (i + 1 != n) System.out.print(sign[i + 1]);
        }
    }
}