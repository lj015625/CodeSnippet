package hackerrank.algorithm.gameTheory;
import java.util.Scanner;


public class GameOfStones
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int c = in.nextInt();
        for(int i = 0; i < c; i++)
        {
            int number = in.nextInt();
            if (number < 2)
            {
                System.out.println("Second");
            }
            else if (number % 7 == 0 || number % 7 == 1)
            {
                System.out.println("Second");
            }
            else
            {
                System.out.println("First");
            }
        }
    }
}
