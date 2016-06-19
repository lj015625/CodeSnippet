package foobar;
public class TreeNodes
{
    public static void main(String[] args)
    {
        // 1 8
        // 2 57 7 * 7 + 7 + 1
        // 3 7 * 7 * 7 + 7 * 7 + 7 + 1
        //
        // 1
        // 1 + N
        //
        // 1 + N + N^2
        // 1 + N + N^2 + N^3
        //
        // 1 + N^1 + N^2 + ... +N^L = (N^(L+1)-1)/(N-1)
        //
        // (N^(L+1)-1) / (N-1)
        int children = 7;
        int level = 2;
        System.out.println(totalNumberOfNodes(level, children));
    }
    
    private static int totalNumberOfNodes(int x, int children)
    {
        int numOfNodes = (int) (Math.pow(children, x + 1) - 1) / (children - 1);
        return numOfNodes;
    }
}
