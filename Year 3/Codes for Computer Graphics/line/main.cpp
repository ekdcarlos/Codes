#include <GL/glut.h>
#include <iostream>

void display(){
	glClear(GL_COLOR_BUFFER_BIT); // clear buffer
	glBegin(GL_LINES); // display a line
	glColor3f(1.0,0.0,0.0); // colour specifications
	glVertex2f(0.0,0.5);
	glEnd();
	glFlush();
}

int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(800,800);
	glutInitWindowPosition(70,70);
	glutCreateWindow("Simple lines");
	glutDisplayFunc(display);
	glutMainLoop();
	return 0;
}

