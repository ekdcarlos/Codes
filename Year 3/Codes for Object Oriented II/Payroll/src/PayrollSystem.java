import java.util.ArrayList;

public class PayrollSystem {
    private ArrayList<Employee> employeeList;

    public PayrollSystem() {
        employeeList = new ArrayList<>();
    }

    public void addEmployee(Employee employee) {
        employeeList.add(employee);
    }

    public void removeEmployee(int id) {
        Employee employeeToRemove = null;
        for (Employee employee : employeeList) {
            if (employee.getId() == id) {
                employeeToRemove = employee;
                break;
            }
        }

        if (employeeToRemove != null) {
            employeeList.remove(employeeToRemove);
            System.out.println("Employee removed successfully!");
        } else {
            System.out.println("Employee with ID " + id + " not found.");
        }
    }

    public void displayEmployees() {
        for (Employee employee : employeeList) {
            System.out.println(employee);
        }
    }

    public void calculatePayroll() {
        double totalPayroll = 0;
        System.out.println("\nCalculating Payroll");
        for (Employee employee : employeeList) {
            double salary = employee.calculateSalary();
            System.out.println(employee.getName() + ": $" + salary);
            totalPayroll += salary;
        }
        System.out.println("Total Payroll: $" + totalPayroll);
    }

    public static void main(String[] args) {
        PayrollSystem payrollSystem = new PayrollSystem();

        // Creating different types of employees
        FullTimeEmployee emp1 = new FullTimeEmployee("Emmanuel Dena", 101, 5000, 1000);
        PartTimeEmployee emp2 = new PartTimeEmployee("Kabarak Moi ", 102, 20, 80);
        Intern emp3 = new Intern("Michaela Joni", 103, 2000, 15);

        // Adding employees to the payroll system
        payrollSystem.addEmployee(emp1);
        payrollSystem.addEmployee(emp2);
        payrollSystem.addEmployee(emp3);

        // Display all employees
        System.out.println("All Employees:");
        payrollSystem.displayEmployees();

        // Calculate and display payroll
        payrollSystem.calculatePayroll();

        // Remove an employee
        payrollSystem.removeEmployee(102);

        // Display remaining employees
        System.out.println("\nRemaining Employees:");
        payrollSystem.displayEmployees();

        // Calculate updated payroll
        payrollSystem.calculatePayroll();
    }
}