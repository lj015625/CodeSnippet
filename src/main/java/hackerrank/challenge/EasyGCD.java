package hackerrank.challenge;

import java.util.Scanner;

public class EasyGCD
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int A[] = new int[n];
        for(int A_i = 0; A_i < n; A_i++)
        {
            A[A_i] = in.nextInt();
        }
        int gcd = A[0];
        for(int i = 1; i < n; i++)
        {
            gcd = gcd(gcd, A[i]);
        }
        // 1 <= l <= k
        int max = k - k % gcd;
        for(int i = 2; i * i <= gcd; i++)
        {
            if(gcd % i == 0)
            {
                max = getBigger(max, k - k % i);
                int divisor2 = gcd / i;
                max = getBigger(max, k - k % divisor2);
            }
        }
        System.out.println(max);
    }

    private static int gcd(int a, int b)
    {
        while(b > 0)
        {
            int y = a % b;
            a = b;
            b = y;
        }
        return a;
    }

    private static int getBigger(int a, int b)
    {
        if(a > b)
        {
            return a;
        }
        return b;
    }
}
