package foobar;
import java.util.ArrayList;
import java.util.List;
/**
 * <p>
 * </p>
 * <p>
 * Copyright &copy 2016 Leonardo Ji
 * </p>
 */
public class PeculiarBalance
{
    public static String[] answer(int x)
    {
        List<Short> result = toBase3(x);
        List<String> results = new ArrayList<String>();
        int curPos = 0;
        int carry = 0;
        while(curPos < result.size())
        {
            // get each digit
            int digit = result.get(curPos);
            int temp = digit + carry;
            // add nothing, carry add 1
            if(3 == temp)
            {
                results.add("-");
                carry = 1;
            }
            // add 1 on the left, carry add 1
            else if(2 == temp)
            {
                results.add("L");
                carry = 1;
            }
            // add 1 on the right to balance left
            else if(1 == temp)
            {
                results.add("R");
                carry = 0;
            }
            else
            {
                results.add("-");
                carry = 0;
            }
            curPos++;
        }
        // the highest digit on the right
        if(carry == 1)
        {
            results.add("R");
        }
        
        String[] resultsArr = new String[results.size()];
        int i = 0;
        for(String str : results)
        {
            resultsArr[i++] = str;
        }
        return resultsArr;
    }

    private static List<Short> toBase3(int x)
    {
        List<Short> result = new ArrayList<Short>();
        int p = 0;
        while(x > 0)
        {
            if(x % 3 == 0)
            {
                result.add((short) 0);
            }
            // the digit is 1 for base3
            if(x % 3 == 1)
            {
                result.add((short) 1);
            }
            // the digit is 2 for base3
            else if(x % 3 == 2)
            {
                result.add((short) 2);
            }
            x = (int) Math.floor(x / 3);
            p++;
        }
        return result;
    }

    public static void main(String[] args)
    {
        int num = 546;
        for(String str : answer(num))
        {
            System.out.print(str);
        }
    }
}
