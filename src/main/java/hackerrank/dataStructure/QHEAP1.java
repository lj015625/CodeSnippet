package hackerrank.dataStructure;
import java.text.ParseException;
import java.util.PriorityQueue;
import java.util.Scanner;

public class QHEAP1
{
    public static void main(String[] args) throws ParseException
    {
        PriorityQueue<Long> queue = new PriorityQueue<Long>();
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for(int i = 0; i < n; i++)
        {
            int op = in.nextInt();
            
            if (op == 1)
            {
                long q = in.nextLong();
                queue.add(q);
            }
            else if (op == 2)
            {
                long q = in.nextLong();
                queue.remove(q);
            }
            else if (op == 3)
            {
                System.out.println(queue.peek());
            }
        }
    }
}
