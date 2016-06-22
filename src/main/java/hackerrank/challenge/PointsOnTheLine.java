package hackerrank.challenge;

import java.util.Scanner;

public class PointsOnTheLine
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] x = new int[n];
        int[] y = new int[n];
        for(int a0 = 0; a0 < n; a0++)
        {
            x[a0] = in.nextInt();
            y[a0] = in.nextInt();
        }

        boolean match = true;
        boolean horizontal = false;
        boolean vertical = false;
        for(int i = 1; i < n; i++)
        {
            if(i == 1)
            {
                if(x[i - 1] == x[i])
                {
                    horizontal = true;
                }
                else if(y[i - 1] == y[i])
                {
                    vertical = true;
                }
                else
                {
                    match = false;
                    break;
                }
            }
            else if(i > 1)
            {
                if(horizontal && x[i - 1] != x[i])
                {
                    match = false;
                    break;
                }
                if(vertical && y[i - 1] != y[i])
                {
                    match = false;
                    break;
                }
            }
        }
        if(match)
        {
            System.out.println("YES");
        }
        else
        {
            System.out.println("NO");
        }
    }
}
