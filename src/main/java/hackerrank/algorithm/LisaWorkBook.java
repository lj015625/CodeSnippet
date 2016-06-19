package hackerrank.algorithm;
import java.util.Scanner;

public class LisaWorkBook
{
    public static void main(String[] args)
    {
        int n, k, special = 0, page = 0;
        Scanner s = new Scanner(System.in);
        n = s.nextInt(); // number of chapters
        k = s.nextInt(); // problems per page
        int[] t = new int[n];
        for(int i = 0; i < n; i++)
        {
            t[i] = s.nextInt(); // number of problems in each chapters
        }
        // each chapter
        for(int i = 0; i < n; i++)
        {
            // each problem
            int currentProblemOnPage = k;
            page++;
            for(int j = 1; j <= t[i]; j++)
            {
                if(currentProblemOnPage == 0)
                {
                    currentProblemOnPage = k;
                    page++;
                }
                currentProblemOnPage--;
                if (page == j)
                {
                    special++;
                }
            }
        }
        System.out.println(special);
    }
}
