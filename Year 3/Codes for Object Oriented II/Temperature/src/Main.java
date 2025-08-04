public class Main {
    public static void main(String[] args) {
        double temperature = Tempinput.getTemperature();
        String state = Statedet.getState(temperature);

        System.out.println("At " + temperature + "°C, water is in a " + state + " state.");
    }
}