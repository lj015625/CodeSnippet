package hackerrank.algorithm.dynamicProgramming;
import java.math.BigInteger;
import java.util.Scanner;

public class FibonacciModified
{
    public static void main(String[] args) throws Exception
    {
        Scanner in = new Scanner(System.in);
        BigInteger a = BigInteger.valueOf(in.nextLong());
        BigInteger b = BigInteger.valueOf(in.nextLong());
        int size = in.nextInt();
        BigInteger end = fib(a, b, 1, size);
        System.out.println(end.toString());
    }

    static BigInteger fib(BigInteger a, BigInteger b, int n, int size)
    {
        if(size <= 1)
        {
            return BigInteger.ONE;
        }
        else if (n == size - 1)
        {
            return b;
        }
        BigInteger c = a.add(b.pow(2));
        return fib(b, c, n + 1, size);
    }
}
