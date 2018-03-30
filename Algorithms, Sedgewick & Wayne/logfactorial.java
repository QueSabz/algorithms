import java.lang.Math;

public class logfactorial
{
    public static double factorial(int N)
    {
        if (N <= 1) return 1;
        else return N * factorial(N-1);
    }

    public static void main(String[] args)
    {
        int N = Integer.parseInt(args[0]);
        StdOut.println(Math.log(factorial(N)));
    }
}