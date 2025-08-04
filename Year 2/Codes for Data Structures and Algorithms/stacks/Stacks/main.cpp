#include <iostream>

using namespace std;

class StackNode{
public:
    int data;
    StackNode*next;
    };
class Stack{
public:
    StackNode*top;
    Stack(){
        top=nullptr;
    }
    void push(int data);
    int pop();
    int peek();
    bool isEmpty();
    };
void Stack::push(int data){
StackNode*newNode = new StackNode();
newNode->next = top;
top = newNode;
cout<<data<<"pushed onto stack\n"<<endl;
}

int Stack::pop(){
if(isEmpty()){
    cout<<"Stack Underflow\n"<<endl;
    return 0;}
    int poppedData = top->data;
    StackNode*temp = top;
    top = top->next;
    delete temp;
    return poppedData;
}

int Stack::peek(){
    if(isEmpty()){
    cout<<"Stack is empty\n"<<endl;
    return 0;}
    return top->data;
}
    bool Stack::isEmpty(){
        return top==nullptr;
    }

int main()
{
    Stack stack;
    stack.push(10);
    stack.push(20);
    stack.push(30);
    stack.push(500);
    cout << stack.pop()<<"popped from stack\n" << endl;
    cout << "Top element is:"<<stack.peek() << endl;
    return 0;
}
