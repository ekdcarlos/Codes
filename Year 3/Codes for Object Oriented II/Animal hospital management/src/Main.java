import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // Create a list to hold animals
        List<Animal> animals = new ArrayList<>();

        // Add different types of animals to the list
        animals.add(new Dog("Kiboso", 3, "Kasabu", "Chihuahua", false));
        animals.add(new Cat("Gunga", 5, "Tamara ", "Long-haired", true));
        animals.add(new Bird("Happy", 2, "Kigunga", "Parrot", true));
        animals.add(new Dog("Chilly", 7, "Mamito", "German Shepherd", true));
        animals.add(new Cat("Kitty", 1, "Geralt", "Fluffy", false));

        // Hospital management operations
        System.out.println("=== Welcome to Animal Hospital Management System ===");
        System.out.println("Total animals in hospital: " + animals.size());
        System.out.println("\nProcessing all animals...\n");

        // Demonstrate polymorphic behavior
        for (Animal animal : animals) {
            System.out.println("----------------------------------");
            animal.examine();
            animal.treat(); // Polymorphic call - different treatment for each animal type

            // Additional animal-specific behaviors
            if (animal instanceof Dog) {
                ((Dog) animal).bark();
            } else if (animal instanceof Cat) {
                ((Cat) animal).purr();
            } else if (animal instanceof Bird) {
                ((Bird) animal).chirp();
            }

            animal.discharge();
            System.out.println("----------------------------------\n");
        }

        System.out.println("All animals have been treated. Hospital session complete.");
    }
}