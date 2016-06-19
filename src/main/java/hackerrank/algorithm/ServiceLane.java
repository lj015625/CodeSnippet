package hackerrank.algorithm;
import java.util.Scanner;

public class ServiceLane
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int t = in.nextInt();
        int[] width = new int[n];
        for (int i = 0; i < n; i++)
        {
            width[i] = in.nextInt();
        }
        for (int j = 0; j < t; j++)
        {
            int start = in.nextInt();
            int end = in.nextInt();
            int min = width[start];
            for (int k = start + 1; k <= end; k++)
            {
                if (width[k] < min)
                {
                    min = width[k];
                }
            }
            System.out.println(min);
        }
    }
}
