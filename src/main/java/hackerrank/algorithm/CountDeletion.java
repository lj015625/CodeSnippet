package hackerrank.algorithm;
import java.util.Scanner;

public class CountDeletion
{
    public static int countDeletions(String s)
    {
        int count = 0;
        char lastChar = 0;
        for (char c : s.toCharArray())
        {
            if (c == lastChar)
            {
                count++;
            }
            else
            {
                lastChar = c;
            }
        }
        return count;
    }

    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int c = in.nextInt();
        
        for(int i = 0; i < c; i++)
        {
            String nextString = in.next();
            System.out.println(countDeletions(nextString));
        }
    }
}
