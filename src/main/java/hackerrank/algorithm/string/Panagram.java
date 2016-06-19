package hackerrank.algorithm.string;
import java.util.Scanner;

public class Panagram
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        String test = in.nextLine();
        int rez = 0;
        for (char c : test.toLowerCase().toCharArray())
        {
            if (c >= 'a' && c <= 'z')
            {
                rez |= 1 << (c - 'a');
            }
        }
        System.out.println(rez == (1 << 26) - 1 ? "pangram" : "not pangram");
    }
}
