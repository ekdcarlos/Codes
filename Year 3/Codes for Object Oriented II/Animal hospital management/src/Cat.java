// Cat subclass
class Cat extends Animal {
    private String furType;
    private boolean isNeutered;

    public Cat(String name, int age, String owner, String furType, boolean isNeutered) {
        super(name, age, owner);
        this.furType = furType;
        this.isNeutered = isNeutered;
    }

    @Override
    public void treat() {
        System.out.println("Treating cat " + getName());
        System.out.println("Fur type: " + furType);
        if (!isNeutered) {
            System.out.println("Recommending neutering procedure...");
        }
        System.out.println("Checking for hairballs...");
        System.out.println("Treating complete for " + getName());
    }

    public void purr() {
        System.out.println(getName() + " says: Purrrrr...");
    }
}

