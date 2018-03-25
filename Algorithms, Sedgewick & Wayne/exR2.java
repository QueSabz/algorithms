public class exR2
{
    public static String exR2(int n)
    {
     if (n <= 0) return "";
     String s = exR2(n-3) + n + exR2(n-2) + n;
     return s;
    }

    public static void main(String[] args)
    {
        int n = Integer.parseInt(args[0]);
        StdOut.println(exR2(n));
    }
}