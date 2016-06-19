package hackerrank.algorithm;
import java.text.ParseException;
import java.util.Scanner;
import java.util.Stack;


public class MaximumStack
{
    public static void main(String[] args) throws ParseException
    {
        Stack<Long> maxStack = new Stack<Long>();
        Stack<Long> stack = new Stack<Long>();
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for(int i = 0; i < n; i++)
        {
            int op = in.nextInt();
            
            if (op == 1)
            {
                long q = in.nextLong();
                stack.push(q);
                if (maxStack.isEmpty())
                {
                    maxStack.push(q);
                }
                else
                {
                    long max = maxStack.peek();
                    if (q >= max)
                    {
                        maxStack.push(q);
                    }
                }
            }
            else if (op == 2)
            {
                long curr = stack.pop();
                if (curr == maxStack.peek())
                {
                    maxStack.pop();
                }
            }
            else if (op == 3)
            {
                System.out.println(maxStack.peek());
            }
        }
    }
}
