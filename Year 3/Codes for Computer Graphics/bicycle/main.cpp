#include <windows.h>
#include <GL/gl.h>
#include <GL/glu.h>
#include <cmath>
#include <iostream>

// Window dimensions
const int WINDOW_WIDTH = 800;
const int WINDOW_HEIGHT = 600;

// Global variables for animation
float bicyclePosition = -200.0f;
float stonePosition = 800.0f;
bool running = true;

// Window procedure
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
        case WM_CLOSE:
            running = false;
            PostQuitMessage(0);
            return 0;
        case WM_KEYDOWN:
            if (wParam == VK_ESCAPE) {
                running = false;
                PostQuitMessage(0);
            }
            return 0;
        case WM_SIZE:
            glViewport(0, 0, LOWORD(lParam), HIWORD(lParam));
            return 0;
    }
    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}

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

// Function to draw a filled rectangle
void drawRectangle(float x1, float y1, float x2, float y2) {
    glBegin(GL_QUADS);
    glVertex2f(x1, y1);
    glVertex2f(x2, y1);
    glVertex2f(x2, y2);
    glVertex2f(x1, y2);
    glEnd();
}

// Function to draw the bicycle
void drawBicycle(float offsetX) {
    // Set line color to white
    glColor3f(1.0f, 0.0f, 0.0f);
    glLineWidth(2.0f);
    
    // Upper body of cycle (frame) - converted coordinates
    drawLine(50 + offsetX, 405, 100 + offsetX, 405);   // Bottom tube
    drawLine(75 + offsetX, 375, 125 + offsetX, 375);   // Top tube
    drawLine(50 + offsetX, 405, 75 + offsetX, 375);    // Seat tube
    drawLine(100 + offsetX, 405, 100 + offsetX, 345);  // Seat post
    drawLine(150 + offsetX, 405, 100 + offsetX, 345);  // Down tube
    drawLine(75 + offsetX, 345, 75 + offsetX, 370);    // Handlebar stem
    drawLine(70 + offsetX, 370, 80 + offsetX, 370);    // Handlebar
    drawLine(80 + offsetX, 345, 100 + offsetX, 345);   // Connecting tube
    
    // Wheels
    drawCircle(150 + offsetX, 405, 30);  // Rear wheel
    drawCircle(50 + offsetX, 405, 30);   // Front wheel
}

// Function to draw the road
void drawRoad() {
    glColor3f(0.5f, 0.5f, 0.8f);  // Gray color for road
    glLineWidth(3.0f);
    drawLine(0, 436, WINDOW_WIDTH, 436);
}

// Function to draw the stone
void drawStone(float offsetX) {
    glColor3f(0.8f, 1.6f, 0.6f);  // Brown color for stone
    drawRectangle(offsetX, 436, offsetX + 20, 431);
}

// Render function
void render() {
    // Clear the screen
    glClear(GL_COLOR_BUFFER_BIT);
    
    // Draw road
    drawRoad();
    
    // Draw bicycle
    drawBicycle(bicyclePosition);
    
    // Draw stone
    drawStone(stonePosition);
    
    glFlush();
}

// Update animation
void updateAnimation() {
    // Move bicycle to the right
    bicyclePosition += 1.0f;
    
    // Move stone to the left
    stonePosition -= 2.0f;
    
    // Reset positions when they go off screen
    if (bicyclePosition > WINDOW_WIDTH + 200) {
        bicyclePosition = -200.0f;
    }
    
    if (stonePosition < -50) {
        stonePosition = WINDOW_WIDTH + 50;
    }
}

// Initialize OpenGL
void initOpenGL() {
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    
    // Set up orthographic projection (similar to original graphics coordinates)
    glOrtho(0, WINDOW_WIDTH, WINDOW_HEIGHT, 0, -1, 1);
    
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    
    // Set background color to black
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    
    // Enable line smoothing
    glEnable(GL_LINE_SMOOTH);
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST);
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, 
                   LPSTR lpCmdLine, int nCmdShow) {
    
    // Register window class
    WNDCLASS wc = {};
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = "OpenGLWindow";
    wc.hCursor = LoadCursor(NULL, IDC_ARROW);
    wc.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);
    
    if (!RegisterClass(&wc)) {
        MessageBox(NULL, "Failed to register window class", "Error", MB_OK);
        return -1;
    }
    
    // Create window
    HWND hwnd = CreateWindow(
        "OpenGLWindow",
        "Moving Bicycle Animation - Dev-C++ OpenGL",
        WS_OVERLAPPEDWINDOW,
        CW_USEDEFAULT, CW_USEDEFAULT,
        WINDOW_WIDTH + 16, WINDOW_HEIGHT + 39, // Account for window borders
        NULL, NULL, hInstance, NULL
    );
    
    if (!hwnd) {
        MessageBox(NULL, "Failed to create window", "Error", MB_OK);
        return -1;
    }
    
    // Get device context
    HDC hdc = GetDC(hwnd);
    
    // Set pixel format
    PIXELFORMATDESCRIPTOR pfd = {};
    pfd.nSize = sizeof(PIXELFORMATDESCRIPTOR);
    pfd.nVersion = 1;
    pfd.dwFlags = PFD_DRAW_TO_WINDOW | PFD_SUPPORT_OPENGL | PFD_DOUBLEBUFFER;
    pfd.iPixelType = PFD_TYPE_RGBA;
    pfd.cColorBits = 24;
    pfd.cDepthBits = 16;
    pfd.iLayerType = PFD_MAIN_PLANE;
    
    int pixelFormat = ChoosePixelFormat(hdc, &pfd);
    SetPixelFormat(hdc, pixelFormat, &pfd);
    
    // Create OpenGL context
    HGLRC hglrc = wglCreateContext(hdc);
    wglMakeCurrent(hdc, hglrc);
    
    // Initialize OpenGL settings
    initOpenGL();
    
    // Show window
    ShowWindow(hwnd, nCmdShow);
    UpdateWindow(hwnd);
    
    // Main message loop
    MSG msg;
    while (running) {
        // Handle Windows messages
        while (PeekMessage(&msg, NULL, 0, 0, PM_REMOVE)) {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
        
        // Update animation
        updateAnimation();
        
        // Render
        render();
        
        // Swap buffers
        SwapBuffers(hdc);
        
        // Control frame rate
        Sleep(16); // ~60 FPS
    }
    
    // Cleanup
    wglMakeCurrent(NULL, NULL);
    wglDeleteContext(hglrc);
    ReleaseDC(hwnd, hdc);
    
    return 0;
}


