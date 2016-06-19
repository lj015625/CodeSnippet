package hackerrank.algorithm.string;
import java.util.Scanner;

public class GameOfThrone1
{

    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        String str = in.next();
        int length = str.length();
        int n = 0;
        for(char character : str.toLowerCase().toCharArray())
        {
            n ^= 1 << character - 'a';
        }
        if(length % 2 == 0)
        {
            if(n > 1)
            {
                System.out.println("NO");
            }
            else
            {
                System.out.println("YES");
            }
        }
        else
        {
            int count = 0;
            boolean palindrome = true;
            for(int i = 0; i < 26; i++)
            {
                if((1 << i & n) > 0)
                {
                    count++;
                    if(count > 1)
                    {
                        palindrome = false;
                        break;
                    }
                }
            }
            if(palindrome)
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
