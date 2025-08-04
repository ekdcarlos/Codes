import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.FileWriter;
import java.io.IOException;

public class StudentInformationForm {
    public static void main(String[] args) {
        // Create the main frame
        JFrame frame = new JFrame("Student Information Form");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);
        frame.setLayout(new BorderLayout());

        // Create a panel for the form
        JPanel formPanel = new JPanel(new GridLayout(4, 2, 10, 10));
        formPanel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));

        // Create form components
        JLabel nameLabel = new JLabel("Name:");
        JTextField nameField = new JTextField();

        JLabel ageLabel = new JLabel("Age:");
        JTextField ageField = new JTextField();

        JLabel courseLabel = new JLabel("Course:");
        JTextField courseField = new JTextField();

        // Add components to form panel
        formPanel.add(nameLabel);
        formPanel.add(nameField);
        formPanel.add(ageLabel);
        formPanel.add(ageField);
        formPanel.add(courseLabel);
        formPanel.add(courseField);

        // Create button panel
        JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 20, 10));
        JButton submitButton = new JButton("Submit");
        JButton clearButton = new JButton("Clear");

        buttonPanel.add(submitButton);
        buttonPanel.add(clearButton);

        // Add panels to frame
        frame.add(formPanel, BorderLayout.CENTER);
        frame.add(buttonPanel, BorderLayout.SOUTH);

        // Submit button action
        submitButton.addActionListener(new ActionListener() {
            @Override
            protected Object clone() throws CloneNotSupportedException {
                return super.clone();
            }

            public void actionPerformed(ActionEvent e) {
                String name = nameField.getText();
                String age = ageField.getText();
                String course = courseField.getText();

                // Validate inputs
                if (name.isEmpty() || age.isEmpty() || course.isEmpty()) {
                    JOptionPane.showMessageDialog(frame, "Please fill in all fields",
                            "Error", JOptionPane.ERROR_MESSAGE);
                    return;
                }

                try {
                    // Validate age is a number
                    int ageValue = Integer.parseInt(age);
                    if (ageValue <= 0) {
                        throw new NumberFormatException();
                    }

                    // Create student information string
                    String studentInfo = String.format("Name: %s, Age: %s, Course: %s%n",
                            name, age, course);

                    // Print to console
                    System.out.print(studentInfo);

                    // Save to file
                    try (FileWriter writer = new FileWriter("students.txt", true)) {
                        writer.write(studentInfo);
                        JOptionPane.showMessageDialog(frame,
                                "Student information saved successfully!",
                                "Success", JOptionPane.INFORMATION_MESSAGE);
                    } catch (IOException ex) {
                        JOptionPane.showMessageDialog(frame,
                                "Error saving to file: " + ex.getMessage(),
                                "Error", JOptionPane.ERROR_MESSAGE);
                    }

                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(frame,
                            "Please enter a valid positive number for age",
                            "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        // Clear button action
        clearButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                nameField.setText("");
                ageField.setText("");
                courseField.setText("");
            }
        });

        // Center and display the frame
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }
}