#include <iostream>
using namespace std;

// Node structure representing each element in the list
class Node {
public:
    int data;      // Data part of the node
    Node* next;    // Pointer to the next node

    Node(int val) {  // Constructor to initialize node\\
        data = val;
        next = nullptr;
    }
};

// LinkedList class to manage the nodes
class LinkedList {
public:
    Node* head;    // Head pointer to track the first node

    LinkedList() {  // Constructor to initialize the linked list
        head = nullptr;
    }

    // Function to insert a node into a sorted linked list
    void insertIntoSortedList(int newVal);

    // Function to insert a node at a given position
    void insertAtPosition(int position, int newVal);

    // Function to print the entire list
    void printList();
};

// Function to insert a node into a sorted list
void LinkedList::insertIntoSortedList(int newVal) {
    Node* newNode = new Node(newVal);  // Create a new node with the given value

    // Case 1: Insert at the beginning if list is empty or new node should be the new head
    if (head == nullptr || head->data >= newVal) {
        newNode->next = head;  // Point the new node's next to the current head
        head = newNode;        // Update the head to the new node
        cout << "Inserted " << newVal << " at the beginning of the list.\n";
        return;
    }

    // Case 2: Traverse the list to find the correct insertion point
    Node* current = head;
    while (current->next != nullptr && current->next->data < newVal) {
        current = current->next;  // Move to the next node
    }

    // Insert the new node after the current node
    newNode->next = current->next;
    current->next = newNode;

    cout << "Inserted " << newVal << " into the sorted list.\n";
}

// Function to insert a node at a given position (0-based index)
void LinkedList::insertAtPosition(int position, int newVal) {
    Node* newNode = new Node(newVal);  // Create a new node with the given value

    // Case 1: Insert at the beginning if position is 0
    if (position == 0) {
        newNode->next = head;  // Point the new node's next to the current head
        head = newNode;        // Update the head to the new node
        cout << "Inserted " << newVal << " at position " << position << ".\n";
        return;
    }

    Node* current = head;
    int count = 0;

    // Traverse the list to find the position just before the desired insertion point
    while (current != nullptr && count < position - 1) {
        current = current->next;
        count++;
    }

    // If we reached the end of the list and the position is out of bounds
    if (current == nullptr) {
        cout << "Position " << position << " is out of bounds.\n";
        return;
    }

    // Insert the new node at the correct position
    newNode->next = current->next;
    current->next = newNode;

    cout << "Inserted " << newVal << " at position " << position << ".\n";
}

// Function to print the entire linked list
void LinkedList::printList() {
    if (head == nullptr) {
        cout << "List is empty.\n";
        return;
    }

    Node* temp = head;
    cout << "Linked List: ";
    while (temp != nullptr) {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "nullptr\n";
}

// Main program to test the linked list operations
int main() {
    LinkedList list;

    // Inserting values into a sorted list
    list.insertIntoSortedList(30);
    list.insertIntoSortedList(10);
    list.insertIntoSortedList(50);
    list.insertIntoSortedList(20);

    // Printing the sorted list
    list.printList();

    // Inserting a value at a specific position
    list.insertAtPosition(2, 25);  // Inserting at position 2 (0-based index)
    list.printList();

    // Trying to insert at an invalid position
    list.insertAtPosition(10, 60);  // Out-of-bounds insertion
    list.printList();

    return 0;
}