package hackerrank.algorithm;
import java.util.PriorityQueue;
import java.util.Scanner;

public class JesseCookie
{
    public static void main(String[] args)
    {
        PriorityQueue<Long> queue = new PriorityQueue<Long>();
        Scanner in = new Scanner(System.in);
        long n = in.nextLong();
        long target = in.nextLong();
        for(long i = 0; i < n; i++)
        {
            long q = in.nextLong();
            queue.add(q);
        }
        int count = 0;
        while(queue.size() >= 2 && queue.peek() < target)
        {
            long first = queue.poll();
            long second = queue.poll();
            long next = first + 2 * second;
            queue.add(next);
            count++;
        }
        if(queue.size() < 2 && queue.peek() < target)
        {
            count = -1;
        }
        System.out.println(count);
    }
}
