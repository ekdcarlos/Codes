import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class StudentInfoForm extends JFrame {
    private JTextField nameField, ageField, courseField;
    private JButton submitButton, clearButton;
    private JLabel statusLabel;

    // Custom exception for form validation
    class FormValidationException extends Exception {
        public FormValidationException(String message) {
            super(message);
        }
    }

    public StudentInfoForm() {
        // Set up the frame
        setTitle("Student Information Form");
        setSize(400, 250);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(10, 10, 10, 10);
        gbc.fill = GridBagConstraints.HORIZONTAL;

        // Initialize components
        JLabel nameLabel = new JLabel("Name:");
        nameField = new JTextField(20);
        JLabel ageLabel = new JLabel("Age:");
        ageField = new JTextField(20);
        JLabel courseLabel = new JLabel("Course:");
        courseField = new JTextField(20);
        submitButton = new JButton("Submit");
        clearButton = new JButton("Clear");
        statusLabel = new JLabel("Enter student information");

        // Add components to frame
        gbc.gridx = 0; gbc.gridy = 0;
        add(nameLabel, gbc);
        gbc.gridx = 1;
        add(nameField, gbc);
        gbc.gridx = 0; gbc.gridy = 1;
        add(ageLabel, gbc);
        gbc.gridx = 1;
        add(ageField, gbc);
        gbc.gridx = 0; gbc.gridy = 2;
        add(courseLabel, gbc);
        gbc.gridx = 1;
        add(courseField, gbc);
        gbc.gridx = 0; gbc.gridy = 3;
        add(submitButton, gbc);
        gbc.gridx = 1;
        add(clearButton, gbc);
        gbc.gridx = 0; gbc.gridy = 4; gbc.gridwidth = 2;
        add(statusLabel, gbc);

        // Submit button action
        submitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    validateAndSave();
                    statusLabel.setText("Data saved successfully!");
                } catch (FormValidationException ex) {
                    statusLabel.setText("Error: " + ex.getMessage());
                } catch (IOException ex) {
                    statusLabel.setText("Error saving to file: " + ex.getMessage());
                } catch (Exception ex) {
                    statusLabel.setText("Unexpected error: " + ex.getMessage());
                }
            }
        });

        // Clear button action
        clearButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    clearForm();
                    statusLabel.setText("Form cleared");
                } catch (Exception ex) {
                    statusLabel.setText("Error clearing form: " + ex.getMessage());
                }
            }
        });
    }

    private void validateAndSave() throws FormValidationException, IOException {
        String name = nameField.getText().trim();
        String ageText = ageField.getText().trim();
        String course = courseField.getText().trim();

        // Validate inputs
        if (name.isEmpty()) {
            throw new FormValidationException("Name cannot be empty");
        }
        if (course.isEmpty()) {
            throw new FormValidationException("Course cannot be empty");
        }

        int age;
        try {
            age = Integer.parseInt(ageText);
            if (age < 16 || age > 100) {
                throw new FormValidationException("Age must be between 16 and 100");
            }
        } catch (NumberFormatException e) {
            throw new FormValidationException("Invalid age format");
        }

        // Create student data string
        String studentData = "Name: " + name + ", Age: " + age + ", Course: " + course;

        // Print to console
        System.out.println(studentData);

        // Save to file
        try (BufferedWriter writer = new BufferedWriter(new FileWriter("students.txt", true))) {
            writer.write(studentData);
            writer.newLine();
        }
    }

    private void clearForm() {
        nameField.setText("");
        ageField.setText("");
        courseField.setText("");
    }

    public static void main(String[] args) {
        // Run GUI on Event Dispatch Thread
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                try {
                    new StudentInfoForm().setVisible(true);
                } catch (Exception e) {
                    System.err.println("Error initializing form: " + e.getMessage());
                }
            }
        });
    }
}