public class Statedet {
    public static String getState(double temperature) {
        if (temperature <= 0) {
            return "solid";
        } else if (temperature < 100) {
            return "liquid";
        } else {
            return "gaseous";
        }
    }
}