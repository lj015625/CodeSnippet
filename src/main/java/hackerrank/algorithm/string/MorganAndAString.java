package hackerrank.algorithm.string;
import java.util.Scanner;

public class MorganAndAString
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int n = Integer.parseInt(in.nextLine());
        for(int count = 0; count < n; count++)
        {
            StringBuilder s = new StringBuilder();
            String stringA = in.nextLine().toUpperCase().trim();
            String stringB = in.nextLine().toUpperCase().trim();
            int lengthA = stringA.length();
            int lengthB = stringB.length();
            int indexA = 0;
            int indexB = 0;

            while(indexA < lengthA && indexB < lengthB)
            {
                if(stringA.charAt(indexA) < stringB.charAt(indexB))
                {
                    s.append(stringA.charAt(indexA++));
                }
                else if(stringA.charAt(indexA) > stringB.charAt(indexB))
                {
                    s.append(stringB.charAt(indexB++));
                }
                else
                {
                    int x = indexA, y = indexB;
                    char a = stringA.charAt(indexA);
                    for(; x < lengthA && y < lengthB; x++, y++)
                    {
                        if(stringA.charAt(x) != stringB.charAt(y))
                        {
                            break;
                        }
                        // Compare char with previous char on stringA. if next char in stringA is
                        // bigger than previous one
                        // then it would be needed to compare to stringB's next char.
                        else if(stringA.charAt(x) > a)
                        {
                            s.append(stringA.substring(indexA, x)).append(stringB.substring(indexB, y));
                            indexA = x;
                            indexB = y;
                            a = stringA.charAt(x);
                        }
                    }
                    // stringA is all gone
                    if(x == lengthA)
                    {
                        s.append(stringB.charAt(indexB));
                        indexB++;
                    }
                    // stringB is all gone
                    else if(y == lengthB)
                    {
                        s.append(stringA.charAt(indexA));
                        indexA++;
                    }
                    else
                    {
                        // stringA has priority over stringB
                        if(stringA.charAt(x) <= stringB.charAt(y))
                        {
                            s.append(stringA.charAt(indexA));
                            indexA++;
                        }
                        else
                        {
                            s.append(stringB.charAt(indexB));
                            indexB++;
                        }
                    }
                }
            }
            //left over
            if(indexA <= lengthA - 1)
            {
                s.append(stringA.substring(indexA));
            }
            if(indexB <= lengthB - 1)
            {
                s.append(stringB.substring(indexB));
            }
            System.out.println(s);
        }
    }
}
