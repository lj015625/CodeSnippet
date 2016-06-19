package hackerrank.algorithm.bitManipulation;
import java.util.Scanner;

public class LonelyInteger
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] a = new int[n];
        for(int count = 0; count < n; count++)
        {
            a[count] = in.nextInt();

        }
        int result = 0;
        for(int i = 0; i < a.length; i++)
        {
            result = result ^ a[i];
        }
        System.out.println(result);
    }
}
