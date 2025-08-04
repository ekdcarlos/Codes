// Main class with try-catch
public class Main {
    public static void main(String[] args) {
        Payment payment;

        try {
            String method = "MPesa"; // You can change to "CreditCard", "PayPal", etc.
            double amount = 1500;

            if (amount <= 0) {
                throw new IllegalArgumentException("Amount must be greater than zero.");
            }

            // Polymorphism: assigning subclass to superclass reference
            switch (method) {
                case "CreditCard":
                    payment = new CreditCardPayment();
                    break;
                case "PayPal":
                    payment = new PayPalPayment();
                    break;
                case "MPesa":
                    payment = new MPesaPayment();
                    break;
                default:
                    throw new Exception("Unsupported payment method: " + method);
            }

            // Execute overridden method
            payment.makePayment(amount);
        } catch (IllegalArgumentException e) {
            System.out.println("Input error: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Processing error: " + e.getMessage());
        } finally {
            System.out.println("Payment process completed.");
        }
    }
}