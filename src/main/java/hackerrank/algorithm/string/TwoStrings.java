package hackerrank.algorithm.string;
import java.util.Scanner;

public class TwoStrings
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int c = in.nextInt();
        int m = 0;
        for(int i = 0; i < c; i++)
        {
            String str1 = in.next();
            String str2 = in.next();
            int n1 = 0;
            for(char character : str1.toLowerCase().toCharArray())
            {
                n1 |= 1 << character - 'a';
            }
            int n2 = 0;
            for(char character : str2.toLowerCase().toCharArray())
            {
                n2 |= 1 << character - 'a';
            }
            m = n1 & n2;
            if(m > 1)
            {
                System.out.println("YES");
            }
            else
            {
                System.out.println("NO");
            }
        }
    }
}
