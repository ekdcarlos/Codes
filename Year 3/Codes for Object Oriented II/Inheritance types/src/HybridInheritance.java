// Hybrid Inheritance: Person implements Interface
interface Creator {
    void createArt();
}

class Base {
    void commonMethod() {
        System.out.println("Base class functionality.");
    }
}

class Hybrid extends Base implements Creator {
    public void createArt() {
        System.out.println("Hybrid class creating art.");
    }
}