package hackerrank.algorithm.string;
import java.util.Scanner;

public class Anagram
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for(int i = 0; i < n; i++)
        {
            String test = in.next();
            if(test.length() % 2 != 0)
            {
                System.out.println("-1");
            }
            else
            {
                int half = test.length() / 2;
                int[] cnt = new int[26];
                String first = test.substring(0, half);
                String second = test.substring(half);
                for(char c : first.toCharArray())
                {
                    cnt[c - 'a']++;
                }
                for(char c : second.toCharArray())
                {
                    cnt[c - 'a']--;
                }
                int count = 0;
                for(int k = 0; k < 26; k++)
                {
                    if(cnt[k] > 0)
                    {
                        count += cnt[k];
                    }
                }
                System.out.println(count);
            }
        }
    }
}
