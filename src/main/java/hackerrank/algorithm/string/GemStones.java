package hackerrank.algorithm.string;
import java.util.Scanner;

public class GemStones
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int c = in.nextInt();
        int m = 0;
        for(int i = 0; i < c; i++)
        {
            String str = in.next();
            int n = 0;
            for(char character : str.toLowerCase().toCharArray())
            {
                n |= 1 << character - 'a';
            }
            if(i == 0)
            {
                m = n;
            }
            else if (i > 0)
            {
                m &= n;
            }
        }
        int count = 0;
        for(int i = 0; i < 26; i++)
        {
            if((1 << i & m ) > 0)
            {
                count++;
            }
        }
        System.out.println(count);
    }
}
