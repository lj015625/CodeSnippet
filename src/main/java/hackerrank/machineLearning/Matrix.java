package hackerrank.machineLearning;
import java.util.Scanner;

public class Matrix
{

    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int a[][] = new int[n][n];
        for(int a_i = 0; a_i < n; a_i++)
        {
            for(int a_j = 0; a_j < n; a_j++)
            {
                a[a_i][a_j] = in.nextInt();
            }
        }
        long firstDiag = 0;
        long secondDiag = 0;
        for(int a_i = 0; a_i < n; a_i++)
        {
            for(int a_j = 0; a_j < n; a_j++)
            {
                if(a_i == a_j)
                {
                    firstDiag += a[a_i][a_j];
                }
                if(a_i + a_j == n - 1)
                {
                    secondDiag += a[a_i][a_j];
                }
            }
        }
        long diff = Math.abs(firstDiag - secondDiag);
        System.out.println(diff);
    }
}
