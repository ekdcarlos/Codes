public class MpesaPayment extends Payment {
    @Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone();
    }
    public void MakePayment(double amount){
        System.out.println("Mpesa payment of KES:" + amount);
    }
}
