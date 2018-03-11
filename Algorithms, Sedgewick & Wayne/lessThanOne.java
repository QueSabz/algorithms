public class lessThanOne
{
    public static void lessThanOne(double x, double y)
    {
        if(0 <= x && x <= 1 && 0 <= y && y <= 1) StdOut.println("True");
        else StdOut.println("False");
    }

    public static void main(String[] args)
    {
        double x = Double.parseDouble(args[0]);
        double y = Double.parseDouble(args[1]);
        lessThanOne(x, y);
    }
}