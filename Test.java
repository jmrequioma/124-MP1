import java.util.Scanner;

public class Test {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        System.out.print("Enter temperature in °F: ");
        float fahrenheit = in.nextFloat();
        float celsius = (fahrenheit - 32) * 5/9;
        
        /* Print result */
        System.out.println("Equivalent temperature in °C: " + celsius);
       
    }
}