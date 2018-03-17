public class lg
{
    public static int largestInt (int N)
    {
        int result = 1;
        int count = 0;
        while (result <= N)
        {
            result *= 2;
            count += 1;
        }
        return count - 1;
    }

    public static void main(String[] args)
    {
        int N = Integer.parseInt(args[0]);
        StdOut.println(largestInt(N));
    }
}