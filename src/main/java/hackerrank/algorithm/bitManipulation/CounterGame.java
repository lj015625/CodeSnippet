package hackerrank.algorithm.bitManipulation;
import java.util.Scanner;

public class CounterGame
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int c = in.nextInt();
        while(c > 0)
        {
            long n = in.nextLong();
            if ((setBits(n-1) & 1) > 0)
            {
                System.out.println("Louise");
            }
            else
            {
                System.out.println("Richard");
            }
            c--;
        }
    }

    private static int setBits(long n)
    {
        int count = 0;
        while(n > 0)
        {
            n &= (n - 1);
            count++;
        }
        return count;
    }
}
