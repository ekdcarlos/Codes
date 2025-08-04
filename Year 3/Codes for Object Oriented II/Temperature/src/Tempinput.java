import java.util.Scanner;

public class Tempinput {
    public static double getTemperature() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the temperature in Celsius: ");
        double temp = scanner.nextDouble();
        scanner.close();
        return temp;
    }
}