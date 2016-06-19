package hackerrank.algorithm.string;
import java.util.Scanner;

public class MakeItAnagram
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        String first = in.next();
        String second = in.next();
        int[] cnt = new int[26];
        for(char c : first.toCharArray())
        {
            cnt[c - 'a']++;
        }
        for(char c : second.toCharArray())
        {
            cnt[c - 'a']--;
        }
        int count = 0;
        for(int j = 0; j < 26; j++)
        {
            if(cnt[j] != 0)
            {
                count += Math.abs(cnt[j]);
            }
        }
        System.out.println(count);
    }
}
