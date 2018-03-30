import java.util.*;
public class fibonacciLong
{
     public static long F(int N)
     {
        if (N == 0) return 0;
        if (N == 1) return 1;
        return F(N-1) + F(N-2);
     }

     public static void main(String[] args)
     {
        ArrayList al = new ArrayList();
        al.add(F(0));
        al.add(F(1));
        for (int N = 2; N < 100; N++)
            al.add((long)al.get(N-1) + (long)al.get(N-2));
            StdOut.println(al);
        StdOut.println(al.size());
     }
}