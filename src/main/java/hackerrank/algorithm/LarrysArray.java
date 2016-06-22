package hackerrank.algorithm;

import java.util.Scanner;

public class LarrysArray
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for(int i = 0; i < n; i++)
        {
            int len = in.nextInt();
            int[] array = new int[len];
            for(int j = 0; j < len; j++)
            {
                array[j] = in.nextInt();
            }
            int count = 0;
            for(int j = 0; j < len; j++)
            {
                for(int k = j + 1; k < len; k++)
                {
                    if(array[j] > array[k])
                    {
                        count++;
                    }
                }
            }
            if(count % 2 == 0)
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
