package hackerrank.algorithm.search;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Dijkstra
{
    public static void main(String[] args)
    {
        int[] neighborX = {0, -1, 0, 1};
        int[] neighborY = {-1, 0, 1, 0};

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        long[][] unvisited = new long[n][n];
        long[][] visited = new long[n][n];
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            {
                unvisited[i][j] = in.nextLong();
                visited[i][j] = Long.MAX_VALUE;
            }
        }

        PriorityQueue<Pos> q = new PriorityQueue<Pos>();
        q.add(new Pos(0, 0, unvisited[0][0]));
        visited[0][0] = unvisited[0][0];
        while(!q.isEmpty())
        {
            Pos pos = q.poll();
            if(visited[pos.y][pos.x] == pos.value)
            {
                // for each neighbor nodes
                for(int i = 0; i < 4; i++)
                {
                    int x = pos.x + neighborX[i];
                    int y = pos.y + neighborY[i];
                    // if neighbor node is smaller than pick it, and add it to priority queue
                    if(x >= 0 && y >= 0 && x < n && y < n && visited[y][x] > visited[pos.y][pos.x] + unvisited[y][x])
                    {
                        visited[y][x] = visited[pos.y][pos.x] + unvisited[y][x];
                        q.add(new Pos(x, y, visited[y][x]));
                    }
                }
            }
        }
        System.out.println(visited[n-1][n-1]);
    }

    static class Pos implements Comparable<Pos>
    {
        private int x;
        private int y;
        private long value;

        public Pos(int x, int y, long value)
        {
            this.x = x;
            this.y = y;
            this.value = value;
        }

        public int compareTo(Pos o)
        {
            return Long.valueOf(value).compareTo(o.value);
        }
    }
}
