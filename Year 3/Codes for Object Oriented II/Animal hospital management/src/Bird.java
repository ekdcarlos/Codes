
// Bird subclass
class Bird extends Animal {
    private String species;
    private boolean canFly;

    public Bird(String name, int age, String owner, String species, boolean canFly) {
        super(name, age, owner);
        this.species = species;
        this.canFly = canFly;
    }

    @Override
    public void treat() {
        System.out.println("Treating bird " + getName());
        System.out.println("Species: " + species);
        System.out.println("Can fly: " + (canFly ? "Yes" : "No"));
        System.out.println("Checking wings and beak...");
        System.out.println("Treating complete for " + getName());
    }

    public void chirp() {
        System.out.println(getName() + " says: Tweet tweet!");
    }
}

