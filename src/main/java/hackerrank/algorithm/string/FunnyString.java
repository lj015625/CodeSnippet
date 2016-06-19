package hackerrank.algorithm.string;
import java.util.Scanner;

public class FunnyString
{
    public static void main(String[] args) throws Exception
    {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int i = 0; i < t; i++)
        {
            String string = in.next();
            int length = string.length();
            boolean funny = true;
            for(int j = 0; j < length / 2; j++)
            {
                if(Math.abs(string.charAt(j) - string.charAt(j + 1)) != Math.abs(string.charAt(length - 1 - j)
                        - string.charAt(length - 2 - j)))
                {
                    funny = false;
                    break;
                }
            }
            if(funny)
            {
                System.out.println("Funny");
            }
            else
            {
                System.out.println("Not Funny");
            }
        }
    }
}
