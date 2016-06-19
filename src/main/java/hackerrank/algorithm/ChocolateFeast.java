package hackerrank.algorithm;
import java.util.Scanner;

public class ChocolateFeast
{
    public static void main(String[] args) throws Exception
    {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int i = 0; i < t; i++)
        {
            int n = in.nextInt();
            int c = in.nextInt();
            int m = in.nextInt();
            int total = n / c;
            // int wrapper = n / c;
            // while(wrapper - m >= 0)
            // {
            //
            //      wrapper -= (m - 1);
            //      total++;
            //
            // }
            // System.out.println(total);

            System.out.println(total + (total - 1) / (m - 1));
        }

        // boughtCandy = money / cost
        // total = boughtCandy + 1 + (boughtCandy - m) / (m - 1)
        // where 1 is the candy we bought for the m we put aside in the first place. This can be
        // simplified as follows:
        //
        // total = boughtCandy + (m - 1)/(m - 1) + (boughtCandy - m) / (m - 1)
        // = boughtCandy + (m - 1 + boughtCandy - m) / ( m - 1 )
        // = boughtCandy + (boughtCandy - 1)/(m - 1)
    }
}
