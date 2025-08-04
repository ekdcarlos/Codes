#include <iostream>
using namespace std;

class StackNode {
public:
    int data;
    StackNode* next;
};

class Stack {
public:
    StackNode* top;
    
    Stack() { top = nullptr; }

    void push(int data);
    int pop();
    int peek();
    bool isEmpty();
};

// Function to push an element onto the stack
void Stack::push(int data) {
    StackNode* newNode = new StackNode();
    newNode->data = data;
    newNode->next = top;
    top = newNode;
    cout << data << " pushed onto stack\n";
}

// Function to pop an element from the stack
int Stack::pop() {
    if (isEmpty()) {
        cout << "Stack Underflow\n";
        return 0;
    }
    int poppedData = top->data;
    StackNode* temp = top;
    top = top->next;
    delete temp;
    return poppedData;
}

// Function to return the top element of the stack
int Stack::peek() {
    if (isEmpty()) {
        cout << "Stack is empty\n";
        return 0;
    }
    return top->data;
}

// Function to check if the stack is empty
bool Stack::isEmpty() {
    return top == nullptr;
}

int main() {
    Stack stack;
    stack.push(10);
    stack.push(20);
    stack.push(30);

    cout << stack.pop() << " popped from stack\n";
    cout << "Top element is " << stack.peek() << endl;

    return 0;
}