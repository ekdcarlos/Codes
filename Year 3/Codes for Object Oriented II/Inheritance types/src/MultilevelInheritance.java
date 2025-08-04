// Multilevel Inheritance: Device → Computer → Laptop
class Device {
    void deviceInfo() {
        System.out.println("This is a generic device.");
    }
}

class Computer extends Device {
    @Override
    void deviceInfo() {
        super.deviceInfo();
        System.out.println("This device is a computer.");
    }
}

class Laptop extends Computer {
    @Override
    void deviceInfo() {
        super.deviceInfo();
        System.out.println("Specifically, it's a laptop.");
    }
}
