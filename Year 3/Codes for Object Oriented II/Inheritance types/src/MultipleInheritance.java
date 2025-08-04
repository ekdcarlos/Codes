// Multiple Inheritance via Interface: Artist + Engineer → CreativeEngineer
interface Artist {
    void createArt();
}

interface Engineer {
    void solveProblem();
}

class CreativeEngineer implements Artist, Engineer {
    public void createArt() {
        System.out.println("Creating a painting.");
    }

    public void solveProblem() {
        System.out.println("Solving a technical problem.");
    }
}