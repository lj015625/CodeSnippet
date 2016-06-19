package hackerrank.algorithm.search;
import java.util.Arrays;
import java.util.Scanner;

public class BinarySearch
{
    public static void main(String[] args) throws Exception
    {
        Scanner in = new Scanner(System.in);
        int key = in.nextInt();
        int size = in.nextInt();
        int[] array = new int[size];
        for(int i = 0; i < size; i++)
        {
            array[i] = in.nextInt();
        }
        Arrays.sort(array);
        int pos = binarySearch(key, size, array);
        System.out.println(pos);
    }

    public static int binarySearch(int key, int size, int[] data)
    {
        int low = 0;
        int high = size - 1;
        while(high >= low)
        {
            int middle = (low + high) / 2;
            if(data[middle] == key)
            {
                return middle;
            }
            if(data[middle] < key)
            {
                low = middle + 1;
            }
            if(data[middle] > key)
            {
                high = middle - 1;
            }
        }
        return -1;
    }
}
