#include <windows.h>
#include <GL/gl.h>
#include <GL/glu.h>
#include <cmath>

const int WIDTH = 800;
const int HEIGHT = 600;

float bikeX = -200.0f;
float cloudX = 100.0f;
float wheelRotation = 0.0f;
bool running = true;

// Declare WindowProc first
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    if (uMsg == WM_CLOSE || (uMsg == WM_KEYDOWN && wParam == VK_ESCAPE)) {
        running = false;
        PostQuitMessage(0);
    }
    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}

// [Rest of your functions...]

// Function to draw a line
void drawLine(float x1, float y1, float x2, float y2) {
    glBegin(GL_LINES);
    glVertex2f(x1, y1);
    glVertex2f(x2, y2);
    glEnd();
}

// Function to draw a circle
void drawCircle(float centerX, float centerY, float radius, int segments = 30) {
    glBegin(GL_LINE_LOOP);
    for (int i = 0; i < segments; i++) {
        float angle = 2.0f * 3.14159f * i / segments;
        float x = centerX + radius * cos(angle);
        float y = centerY + radius * sin(angle);
        glVertex2f(x, y);
    }
    glEnd();
}

void drawRotatingWheel(float centerX, float centerY, float radius, float rotationAngle, int spokeCount) {
    // Wheel rim
    glBegin(GL_LINE_LOOP);
    for (int i = 0; i < 360; i += 10) {
        float angle = i * 3.14159f / 180;
        glVertex2f(centerX + radius * cos(angle), centerY + radius * sin(angle));
    }
    glEnd();
    
    // Spokes with rotation
    glBegin(GL_LINES);
    for (int i = 0; i < spokeCount; i++) {
        float spokeAngle = rotationAngle + (i * (2 * 3.14159f / spokeCount));
        glVertex2f(centerX, centerY);
        glVertex2f(centerX + radius * cos(spokeAngle), centerY + radius * sin(spokeAngle));
    }
    glEnd();
    
    // Wheel hub
    glBegin(GL_POLYGON);
    for (int i = 0; i < 360; i += 30) {
        float angle = i * 3.14159f / 180;
        glVertex2f(centerX + 5 * cos(angle), centerY + 5 * sin(angle));
    }
    glEnd();
}

void drawBicycle(float offsetX) {
    // Set line color to black
    glColor3f(0.0f, 0.0f, 0.0f);
    glLineWidth(2.0f);
    
    // Frame
    drawLine(50 + offsetX, 405, 100 + offsetX, 405);
    drawLine(75 + offsetX, 375, 125 + offsetX, 375);
    drawLine(50 + offsetX, 405, 75 + offsetX, 375);
    drawLine(100 + offsetX, 405, 100 + offsetX, 345);
    drawLine(150 + offsetX, 405, 100 + offsetX, 345);
    drawLine(75 + offsetX, 345, 75 + offsetX, 370);
    drawLine(70 + offsetX, 370, 80 + offsetX, 370);
    drawLine(80 + offsetX, 345, 100 + offsetX, 345);
    
    // Draw rotating wheels
    const float wheelRadius = 30.0f;
    drawRotatingWheel(50 + offsetX, 405, wheelRadius, wheelRotation, 8);  // Front wheel
    drawRotatingWheel(150 + offsetX, 405, wheelRadius, wheelRotation, 8); // Rear wheel
}

void update() {
    const float rotationSpeed = 0.05f;
    
    bikeX += 2.0f;
    cloudX += 0.7f;
    wheelRotation -= bikeX * rotationSpeed;
    
    if (bikeX > WIDTH + 200) {
        bikeX = -200;
        wheelRotation = 0.0f;
    }
    if (cloudX > WIDTH + 100) cloudX = -100;
}

void drawCloud(float x) {
    glColor3f(1.0f, 1.0f, 1.0f);
    glBegin(GL_POLYGON);
    for (int i = 0; i < 360; i += 10) {
        float angle = i * 3.14159f / 180;
        glVertex2f(x + 40 * cos(angle), 100 + 30 * sin(angle));
    }
    glEnd();
}

void drawTree(float x, float baseY) {
    // Trunk
    glColor3f(0.4f, 0.2f, 0.0f);
    glBegin(GL_QUADS);
    glVertex2f(x - 8, baseY);
    glVertex2f(x + 8, baseY);
    glVertex2f(x + 8, baseY - 40);
    glVertex2f(x - 8, baseY - 40);
    glEnd();
    
    // Leaves
    glColor3f(0.2f, 0.7f, 0.2f);
    glBegin(GL_TRIANGLE_FAN);
    glVertex2f(x, baseY - 60);
    for (int i = 0; i <= 360; i += 30) {
        float angle = i * 3.14159f / 180;
        glVertex2f(x + 25 * cos(angle), baseY - 40 + 20 * sin(angle));
    }
    glEnd();
}

void drawScene() {
    // Set light blue background
    glClearColor(0.7f, 0.9f, 1.0f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT);
    
    // Draw ground
    glColor3f(0.4f, 0.8f, 0.4f);
    glBegin(GL_QUADS);
    glVertex2f(0, 420);
    glVertex2f(WIDTH, 420);
    glVertex2f(WIDTH, HEIGHT);
    glVertex2f(0, HEIGHT);
    glEnd();
    
    // Road
    glColor3f(0.2f, 0.2f, 0.2f);
    glBegin(GL_QUADS);
    glVertex2f(0, 430);
    glVertex2f(WIDTH, 430);
    glVertex2f(WIDTH, 450);
    glVertex2f(0, 450);
    glEnd();
    
    // Road markings
    glColor3f(1.0f, 1.0f, 0.0f);
    for (int i = 0; i < WIDTH; i += 60) {
        glBegin(GL_QUADS);
        glVertex2f(i, 440);
        glVertex2f(i + 30, 440);
        glVertex2f(i + 30, 443);
        glVertex2f(i, 443);
        glEnd();
    }
    
    // Trees
    for (int i = 100; i < WIDTH; i += 150) {
        drawTree(i, 430);
    }
    
    // Cloud
    drawCloud(cloudX);
    
    // Bicycle
    drawBicycle(bikeX);
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    WNDCLASS wc = {};
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = "BikeWindow";
    wc.style = CS_OWNDC;
    RegisterClass(&wc);
    
    HWND hwnd = CreateWindow("BikeWindow", "Bicycle Animation", WS_OVERLAPPEDWINDOW,
                             CW_USEDEFAULT, CW_USEDEFAULT, WIDTH, HEIGHT, NULL, NULL, hInstance, NULL);
    
    HDC hdc = GetDC(hwnd);
    
    PIXELFORMATDESCRIPTOR pfd = {
        sizeof(PIXELFORMATDESCRIPTOR),
        1,
        PFD_DRAW_TO_WINDOW | PFD_SUPPORT_OPENGL | PFD_DOUBLEBUFFER,
        PFD_TYPE_RGBA,
        32,
        0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0,
        24,
        0, 0,
        PFD_MAIN_PLANE,
        0,
        0, 0, 0
    };
    
    int pixelFormat = ChoosePixelFormat(hdc, &pfd);
    SetPixelFormat(hdc, pixelFormat, &pfd);
    
    HGLRC hglrc = wglCreateContext(hdc);
    wglMakeCurrent(hdc, hglrc);
    
    glViewport(0, 0, WIDTH, HEIGHT);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0, WIDTH, HEIGHT, 0, -1, 1);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    
    ShowWindow(hwnd, nCmdShow);
    UpdateWindow(hwnd);
    
    MSG msg;
    while (running) {
        while (PeekMessage(&msg, NULL, 0, 0, PM_REMOVE)) {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
        
        update();
        drawScene();
        SwapBuffers(hdc);
        Sleep(16);
    }
    
    wglMakeCurrent(NULL, NULL);
    wglDeleteContext(hglrc);
    ReleaseDC(hwnd, hdc);
    
    return 0;
}
