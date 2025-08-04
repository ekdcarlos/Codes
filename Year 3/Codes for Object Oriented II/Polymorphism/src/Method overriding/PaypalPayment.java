public class PaypalPayment extends Payment{
    @Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone();
    }

    public void MakePayment(double amount){
        System.out.println("Processing Paypal payment of KES:" + amount);
    }
}
