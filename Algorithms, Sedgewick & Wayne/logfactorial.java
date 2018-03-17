import java.lang.Math;

public class logfactorial
{
    public static double logfactorial(int N)
    {
        if (N <= 1) return 1;
        else return N * logfactorial(N-1);
    }

    public static void main(String[] args)
    {
        int N = Integer.parseInt(args[0]);
        StdOut.println(Math.log(logfactorial(N)));
    }
}