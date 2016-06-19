package hackerrank.java;


import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class TimeFormat
{

    public static void main(String[] args) throws ParseException
    {
        Scanner in = new Scanner(System.in);
        String time = in.next();

        SimpleDateFormat dtf = new SimpleDateFormat("hh:mm:ssa");
        Date date = dtf.parse(time);

        SimpleDateFormat dtfOut = new SimpleDateFormat("HH:mm:ss");
        System.out.println(dtfOut.format(date));
    }
}
