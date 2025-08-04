//single inheritance
class Animal{
    void speak(){
        System.out.println("Animal makes a sound");
    }
}
class Dog extends Animal{
    void  bark(){
        System.out.println("Dog barks");
    }
}
public class Main {
    public static void main(String[] args) {
    Dog myDog = new Dog();
    myDog.speak();
    myDog.bark();
    }
}