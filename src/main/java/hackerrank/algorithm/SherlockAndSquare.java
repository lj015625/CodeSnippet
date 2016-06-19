package hackerrank.algorithm;
import java.util.Scanner;

public class SherlockAndSquare
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int c = in.nextInt();
        for(int i = 0; i < c; i++)
        {
            int a = in.nextInt();
            int b = in.nextInt();
            int count = (int) Math.floor(Math.sqrt(b)) - (int) Math.ceil(Math.sqrt(a)) + 1;
            System.out.println(count);
        }
    }
}
