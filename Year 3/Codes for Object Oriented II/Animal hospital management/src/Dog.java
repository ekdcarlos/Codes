// Dog subclass
class Dog extends Animal {
    private String breed;
    private boolean isVaccinated;

    public Dog(String name, int age, String owner, String breed, boolean isVaccinated) {
        super(name, age, owner);
        this.breed = breed;
        this.isVaccinated = isVaccinated;
    }

    @Override
    public void treat() {
        System.out.println("Treating dog " + getName());
        System.out.println("Breed: " + breed);
        if (!isVaccinated) {
            System.out.println("Administering vaccinations...");
            isVaccinated = true;
        }
        System.out.println("Checking for fleas and ticks...");
        System.out.println("Treating complete for " + getName());
    }

    public void bark() {
        System.out.println(getName() + " says: Woof woof!");
    }
}