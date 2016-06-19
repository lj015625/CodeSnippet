package hackerrank.algorithm;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class CutTheStick
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        List<Integer> array = new LinkedList<Integer>();
        for(int i = 0; i < n; i++)
        {
            array.add(in.nextInt());
        }
        Collections.sort(array);
        int previous = 0;
        System.out.println(n);
        int count = 1;
        for(int i : array)
        {
            if(previous > 0)
            {
                if(previous == i)
                {
                    count++;
                }
                else if(previous < i)
                {
                    System.out.println(n - count);
                    n = n - count;
                    count = 1;
                }
            }
            previous = i;
        }
    }
}
