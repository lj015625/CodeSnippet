package hackerrank.algorithm.graphTheory;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class BfsShortestPath
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        in.nextLine();
        StringBuilder output = new StringBuilder();
        for(int k = 0; k < t; k++)
        {
            int n = in.nextInt();
            List<Node> nodes = new ArrayList<Node>();
            for(int i = 1; i <= n; i++)
            {
                Node node = new Node(i);
                nodes.add(node);
            }
            int m = in.nextInt();
            for(int i = 0; i < m; i++)
            {
                in.nextLine();
                int parent = in.nextInt();
                int child = in.nextInt();

                nodes.get(parent - 1).neighbors.add(nodes.get(child - 1));
                nodes.get(child - 1).neighbors.add(nodes.get(parent - 1));
            }
            in.nextLine();
            int s = in.nextInt();
            bfs(nodes.get(s - 1));
            for(int i = 0; i < n; i++)
            {
                if(i != s - 1)
                {
                    output.append(nodes.get(i).visited ? nodes.get(i).cost : -1);
                    output.append(" ");
                }
            }
            output.append("\n");
        }
        System.out.println(output.toString());
    }

    static class Node
    {
        int name;
        boolean visited = false;
        long cost = Long.MAX_VALUE;
        List<Node> neighbors = new LinkedList<Node>();

        public Node(int c)
        {
            this.name = c;
        }
    }

    private static void bfs(Node rootNode)
    {
        Queue<Node> queue = new LinkedList<Node>();
        rootNode.visited = true;
        rootNode.cost = 0;
        queue.add(rootNode);
        while(!queue.isEmpty())
        {
            Node currentNode = queue.peek();
            Node neighbor = getUnvisitedNeighborNode(currentNode);
            if(neighbor != null)
            {
                if(!neighbor.visited)
                {
                    neighbor.visited = true;
                    neighbor.cost = currentNode.cost + 6;
                    queue.add(neighbor);
                }
                // find a shorter path then remove current node and use the neighbor node instead.
                else if(neighbor.visited && neighbor.cost < currentNode.cost + 6)
                {
                    queue.remove();
                    queue.add(neighbor);
                }
            }
            else
            {
                queue.remove();
            }
        }
    }

    private static Node getUnvisitedNeighborNode(Node n)
    {
        for(Node child : n.neighbors)
        {
            if(!child.visited)
            {
                return child;
            }
        }
        return null;
    }
}