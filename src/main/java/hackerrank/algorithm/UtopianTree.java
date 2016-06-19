package hackerrank.algorithm;
import java.util.Scanner;

public class UtopianTree
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int c = in.nextInt();
        for(int count = 0; count < c; count++)
        {
            int n = in.nextInt();
            long length = 1;
            for (int i = 0; i < n; i++)
            {
                if (i % 2 == 1)
                {
                   length++;
                }
                else
                {
                    length *= 2;
                }
            }
            long answer = ((long) Math.pow(2, (n + 3) / 2)) + (((long) Math.pow(-1, n)) - 3) / 2;
            System.out.println(answer);
        }
    }
}
