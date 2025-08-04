#include <GL/glut.h>
void display(){
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(0.0,0.8,1.0);
	glBegin(GL_POLYGON);
	glVertex2f(0.3,0.0);
	glVertex2f(0.15,0.26);
	glVertex2f(-0.15,0.26);
	glVertex2f(-0.3,0.0);
	glVertex2f(-0.15,-0.26);
	glVertex2f(-0.15,0.26);
	glEnd();
	glFlush();
}

void Init(){
	glClearColor(0.1,1.0,0.2,0.2);
	glEnable(GL_POLYGON_SMOOTH);
	glHint(GL_POLYGON_SMOOTH_HINT,GL_NICEST);
}

int main(int argc, char** argv){
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowPosition(100,100);
	glutInitWindowSize(700,700);
	glutCreateWindow("Hexagon");
	glutDisplayFunc(display);
	Init();
	glutMainLoop();
	return 0;
}
