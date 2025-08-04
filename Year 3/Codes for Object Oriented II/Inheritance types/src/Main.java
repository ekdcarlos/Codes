public class Main {
    public static void main(String[] args) {
        System.out.println("== Single Inheritance ==");
        Student student = new Student();
        student.introduce();

        System.out.println("\n== Multilevel Inheritance ==");
        Laptop laptop = new Laptop();
        laptop.deviceInfo();

        System.out.println("\n== Hierarchical Inheritance ==");
        Dog dog = new Dog();
        dog.speak();
        Cat cat = new Cat();
        cat.speak();

        System.out.println("\n== Multiple Inheritance via Interface ==");
        CreativeEngineer ce = new CreativeEngineer();
        ce.createArt();
        ce.solveProblem();

        System.out.println("\n== Hybrid Inheritance ==");
        Hybrid hybrid = new Hybrid();
        hybrid.commonMethod();
        hybrid.createArt();
    }
}