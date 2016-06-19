package hackerrank.algorithm;
import java.util.Scanner;

public class SherlockAndBeast
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int c = in.nextInt();
        while(c > 0)
        {
            int n = in.nextInt();
            StringBuilder builder = new StringBuilder();
            int reminder = n % 3;
            if(reminder == 0)
            {
                for(int j = 0; j < n; j++)
                {
                    builder.append("5");
                }
            }
            else
            {
                for(int k = reminder; k <= n; k = k + 3)
                {
                    if(k % 5 == 0)
                    {
                        for(int numberOfFive = 0; numberOfFive < n - k; numberOfFive++)
                        {
                            builder.append("5");
                        }
                        for(int numberOfThree = 0; numberOfThree < k; numberOfThree++)
                        {
                            builder.append("3");
                        }
                        break;
                    }
                }
                if(builder.length() == 0)
                {
                    builder.append("-1");
                }
            }
            System.out.println(builder.toString());
            c--;
        }
    }
}
