import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(hasAlternatingBits3(5));
    }

    public static boolean hasAlternatingBits3(int n) {
        String bi = Integer.toBinaryString(n);
        for (int i = 0; i < bi.length() - 1; i++)
            if (bi.charAt(i) == bi.charAt(i + 1))
                return false;
        return true;
    }

    public static boolean hasAlternatingBits2(int n) {
        while (n > 0) {
            int cur = n % 2;
            n /= 2;
            if (cur == n % 2) return false;
        }
        return true;
    }

    public static boolean hasAlternatingBits(int n) {
        int cur = n & 1;
        while (n != 0) {
            if ((cur & 1) != (n & 1)) return false;
            n >>= 1;
            cur += 1;
        }
        return true;
    }
}
