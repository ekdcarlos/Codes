public class Vehicle {
    protected int year_of_manufacture;
    protected String model;

    public Vehicle(int x, String y) {
        this.year_of_manufacture = x;
        this.model = y;
    }

    public void displayDetails() {
        System.out.println("Year of manufacture:" + year_of_manufacture);
        System.out.println("The model of car:" + model);
    }
}

