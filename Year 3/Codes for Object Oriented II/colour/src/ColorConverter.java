import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class ColorConverter extends JFrame implements WindowListener {
    private JLabel colorNameLabel;

    public ColorConverter() {
        setTitle("Color Picker");
        setSize(400, 250);
        setLayout(new BorderLayout());
        addWindowListener(this);

        // Create and configure the label
        colorNameLabel = new JLabel("Selected color will appear here", JLabel.CENTER);
        colorNameLabel.setFont(new Font("Arial", Font.BOLD, 20));
        add(colorNameLabel, BorderLayout.CENTER);

        // Add exit button at bottom
        JButton exitBtn = new JButton("Exit");
        exitBtn.addActionListener(e -> System.exit(0));
        add(exitBtn, BorderLayout.SOUTH);

        setVisible(true);

        // Show color picker immediately
        showColorPicker();
    }

    private void showColorPicker() {
        Color selectedColor = JColorChooser.showDialog(
                this,
                "Pick a Color",
                Color.WHITE
        );

        if (selectedColor != null) {
            String colorName = getColorName(selectedColor);
            colorNameLabel.setText(colorName);
            colorNameLabel.setForeground(selectedColor);
        } else {
            colorNameLabel.setText("No color selected");
            colorNameLabel.setForeground(Color.BLACK);
        }
    }

    private String getColorName(Color color) {
        // Basic color names - you can add more
        if (color.equals(Color.RED)) return "Red";
        if (color.equals(Color.GREEN)) return "Green";
        if (color.equals(Color.BLUE)) return "Blue";
        if (color.equals(Color.YELLOW)) return "Yellow";
        if (color.equals(Color.BLACK)) return "Black";
        if (color.equals(Color.WHITE)) return "White";
        if (color.equals(Color.ORANGE)) return "Orange";
        if (color.equals(Color.PINK)) return "Pink";
        if (color.equals(Color.CYAN)) return "Cyan";
        if (color.equals(Color.MAGENTA)) return "Magenta";
        if (color.equals(Color.GRAY)) return "Gray";

        // For custom colors
        return "Custom Color (R:" + color.getRed() +
                " G:" + color.getGreen() +
                " B:" + color.getBlue() + ")";
    }

    // WindowListener methods
    public void windowClosing(WindowEvent e) { System.exit(0); }
    public void windowActivated(WindowEvent e) {}
    public void windowDeactivated(WindowEvent e) {}
    public void windowDeiconified(WindowEvent e) {}
    public void windowIconified(WindowEvent e) {}
    public void windowOpened(WindowEvent e) {}
    public void windowClosed(WindowEvent e) {}

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new ColorConverter());
    }
}