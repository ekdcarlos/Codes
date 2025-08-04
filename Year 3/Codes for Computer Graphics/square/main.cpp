#include <GL/glut.h>

void display() {
    // Clear the screen with black color
    glClearColor(0.0, 0.0, 0.0, 1.0); // Black background
    glClear(GL_COLOR_BUFFER_BIT);
    
    // Set drawing color to red
    glColor3f(1.0, 0.0, 0.0); // Red color
    
    // Draw a square
    glBegin(GL_QUADS);
        glVertex2f(-0.5, -0.5); // Bottom-left corner
        glVertex2f(0.5, -0.5);  // Bottom-right corner
        glVertex2f(0.5, 0.5);   // Top-right corner
        glVertex2f(-0.5, 0.5);  // Top-left corner
    glEnd();
    
    glFlush();
}

int main(int argc, char** argv) {
    // Initialize GLUT
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    
    // Create a window
    glutInitWindowSize(500, 500);
    glutCreateWindow("Red Square on Black Background");
    
    // Set the display callback
    glutDisplayFunc(display);
    
    // Enter the main loop
    glutMainLoop();
    
    return 0;
}
