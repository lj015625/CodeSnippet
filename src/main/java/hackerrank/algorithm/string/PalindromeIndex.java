package hackerrank.algorithm.string;

import java.util.Scanner;

public class PalindromeIndex
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for(int k = 0; k < n; k++)
        {
            String str = in.next();
            int length = str.length();
            int p = -1;
            int i = 0, j = length - 1;
            while(i < length / 2 && j > length / 2)
            {
                // find non-palindrome index
                if(str.charAt(i) != str.charAt(j))
                {
                    if(str.charAt(i + 1) == str.charAt(j) && str.charAt(i + 2) == str.charAt(j - 1))
                    {
                        p = i;
                        i += 2;
                        j--;
                    }
                    else if(str.charAt(i) == str.charAt(j - 1) && str.charAt(i + 1) == str.charAt(j - 2))
                    {
                        p = j;
                        i++;
                        j -= 2;
                    }
                    else
                    {
                        p = -1;
                        break;
                    }
                }
                else
                {
                    i++;
                    j--;
                }
            }
            System.out.println(p);
        }
    }
}