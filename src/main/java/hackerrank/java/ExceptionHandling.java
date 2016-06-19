package hackerrank.java;
import java.text.ParseException;
import java.util.InputMismatchException;
import java.util.Scanner;

public class ExceptionHandling
{
    public static void main(String[] args) throws ParseException
    {
        try
        {
            Scanner in = new Scanner(System.in);
            int num1 = in.nextInt();
            int num2 = in.nextInt();

            int ratio = num1 / num2;
            System.out.println(ratio);
        }
        catch(InputMismatchException e)
        {
            System.out.println("java.util.InputMismatchException");
        }
        catch(ArithmeticException e)
        {
            System.out.println("java.lang.ArithmeticException: / by zero");
        }
    }
}
