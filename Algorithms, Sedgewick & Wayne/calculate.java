public class calculate
{
    public static void main(String[] args)
    {
        StdOut.println((0 + 15) / 2);
        StdOut.println(2.0e-6 * 100000000.1);
        StdOut.println(true && false || true && true);
        double a = (1 + 2.236) / 2;
        double b = 1 + 2 + 3 + 4.0;
        boolean c = 4.1 >= 4;
        String d = 1 + 2 + "3";
        StdOut.println(a + " is of type: " + ((Object)a).getClass().getName());
        StdOut.println(b + " is of type: " + ((Object)b).getClass().getName());
        StdOut.println(c + " is of type: " + ((Object)c).getClass().getName());
        StdOut.println(d + " is of type: " + ((Object)d).getClass().getName());
    }
}