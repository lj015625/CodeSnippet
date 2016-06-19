package hackerrank.algorithm.bitManipulation;
import java.util.Scanner;

public class MaxXor
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int l = in.nextInt();
        int r = in.nextInt();
        int xor = l ^ r;
        int result = xor;
        while(xor >> 1 > 0)
        {
            xor = xor >> 1;
            result |= xor;
        }
        System.out.println(result);
        xor = l ^ r;
        xor |= xor >> 1;
        xor |= xor >> 2;
        xor |= xor >> 4;
        xor |= xor >> 8;
        xor |= xor >> 16;
        System.out.println(result);
    }
}
