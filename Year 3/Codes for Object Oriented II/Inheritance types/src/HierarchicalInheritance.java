// Hierarchical Inheritance: Animal → Dog, Cat
class Animal {
    void speak() {
        System.out.println("Some animal sound.");
    }
}

class Dog extends Animal {
    @Override
    void speak() {
        System.out.println("Dog says: Woof!");
    }
}

class Cat extends Animal {
    @Override
    void speak() {
        System.out.println("Cat says: Meow!");
    }
}