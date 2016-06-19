package hackerrank.algorithm;
import java.text.ParseException;
import java.util.Scanner;


public class Staircase
{
    public static void main(String[] args) throws ParseException
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for (int i = 0; i < n; i++)
        {
            StringBuilder builder = new StringBuilder();
            for (int j = n-1; j > i; j--)
            {
                builder.append(" ");
            }
            for (int k = 0; k <= i; k++)
            {
                builder.append("#");
            }
            System.out.println(builder.toString());
        }
    }
}
