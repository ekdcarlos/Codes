// Abstract base class for all animals
abstract class Animal {
    private String name;
    private int age;
    private String owner;

    public Animal(String name, int age, String owner) {
        this.name = name;
        this.age = age;
        this.owner = owner;
    }

    // Abstract method for treatment
    public abstract void treat();

    // Common methods for all animals
    public void examine() {
        System.out.println("Examining " + name + "...");
        System.out.println("Age: " + age);
        System.out.println("Owner: " + owner);
    }

    public void discharge() {
        System.out.println(name + " is being discharged. Goodbye!");
    }

    // Getters
    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public String getOwner() {
        return owner;
    }
}

