public class equal
{
    public static void isEqual(int a, int b, int c)
    {
        if(a == b && b == c) StdOut.println("Equal");
        else StdOut.println("Not Equal");
    }

    public static void main(String[] args)
    {
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        int c = Integer.parseInt(args[2]);
        isEqual(a, b, c);
    }
}
