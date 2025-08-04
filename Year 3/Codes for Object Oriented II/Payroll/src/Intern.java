public class Intern extends Employee {
    private double stipend;
    private int daysWorked;
    private static final int WORK_DAYS_IN_MONTH = 22;

    public Intern(String name, int id, double stipend, int daysWorked) {
        super(name, id);
        this.stipend = stipend;
        this.daysWorked = daysWorked;
    }

    @Override
    public double calculateSalary() {
        return (stipend / WORK_DAYS_IN_MONTH) * daysWorked;
    }

    public double getStipend() {
        return stipend;
    }

    public int getDaysWorked() {
        return daysWorked;
    }
}
