package hackerrank.algorithm;
import java.util.Scanner;

public class TheTimeInWords
{
    public static void main(String[] args)
    {
        String hours[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"};

        String minutes[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
                "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninteen", "twenty", "twenty one",
                "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight",
                "twenty nine"};

        Scanner in = new Scanner(System.in);
        int hour = in.nextInt();
        String minuteString = in.next();
        int minute = 0;
        if(minuteString.startsWith("0"))
        {
            minute = Integer.parseInt(minuteString.substring(1));
        }
        else
        {
            minute = Integer.parseInt(minuteString);
        }
        StringBuilder timeBuilder = new StringBuilder();
        if(minute == 0)
        {
            timeBuilder.append(hours[hour - 1]).append(" o' clock");
        }
        else if(minute == 15)
        {
            timeBuilder.append("quarter past ").append(hours[hour - 1]);
        }
        else if(minute == 30)
        {
            timeBuilder.append("half past ").append(hours[hour - 1]);
        }
        else if(minute == 45)
        {
            timeBuilder.append("quarter to ").append(hours[hour]);
        }
        else if(minute == 1)
        {
            timeBuilder.append(minutes[0]).append(" minute past ").append(hours[hour - 1]);
        }
        else if(minute < 30)
        {
            timeBuilder.append(minutes[minute - 1]).append(" minutes past ").append(hours[hour - 1]);
        }
        else if(minute > 30 && minute < 60)
        {
            timeBuilder.append(minutes[59 - minute]).append(" minutes to ").append(hours[hour]);
        }
        System.out.println(timeBuilder.toString());
    }
}