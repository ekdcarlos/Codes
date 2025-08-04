public class CreditCardPayment extends Payment {
    @Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone();
    }

    public void MakePayment(double amount){
        System.out.println("Creditcard processing of KES:" + amount);
    }
}
