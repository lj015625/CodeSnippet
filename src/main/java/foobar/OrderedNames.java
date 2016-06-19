package foobar;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
/**
 * <p>
 * </p>
 * <p>
 * Copyright &copy 2016 Leonardo Ji
 * </p>
 */
public class OrderedNames
{
    public static void main(String[] args)
    {
        // Inputs:
        // (string list) names = ["annie", "bonnie", "liz"]
        // Output:
        // (string list) ["bonnie", "liz", "annie"]
        //
        // Inputs:
        // (string list) names = ["abcdefg", "vi"]
        // Output:
        // (string list) ["vi", "abcdefg"]

        String[] names = {"annie", "bonnie", "liz", "al", "cj"};
        answer(names);
    }

    public static String[] answer(String[] names) { 
        Map<Integer, List<String>> namesMap = new TreeMap<Integer, List<String>>();
        for(String name : names)
        {
            int weight = 0;
            for(char alph : name.toCharArray())
            {
                weight += alph;
            }
            List<String> equalWeightNames = namesMap.get(weight);
            if(equalWeightNames == null)
            {
                equalWeightNames = new ArrayList<String>();
                namesMap.put(weight, equalWeightNames);
            }
            equalWeightNames.add(name);
        }
        List<String> orderedNames = new ArrayList<String>();
        for(List<String> equalWeightNames : namesMap.values())
        {
            if(equalWeightNames.size() > 1)
            {
                Collections.sort(equalWeightNames);
            }
            orderedNames.addAll(equalWeightNames);
        }
        String[] orderNamesArray = new String[orderedNames.size()];
        int i = orderedNames.size() - 1;
        for (String name : orderedNames)
        {
            orderNamesArray[i] = name;
            i--;
        }
        return orderNamesArray;
    }
}
