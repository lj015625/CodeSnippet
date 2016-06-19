package hackerrank.algorithm.string;
import java.util.Scanner;

public class LoveLetterMystery
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for(int i = 0; i < n; i++)
        {
            String test = in.next();
            int length = test.length();
            int count = 0;
            int half = length / 2;
            for(int j = 0; j < half; j++)
            {
                count += Math.abs(test.charAt(length - 1 - j) - test.charAt(j));
            }
            System.out.println(count);
        }
    }
}
