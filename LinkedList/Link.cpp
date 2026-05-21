#include <iostream>
using namespace std;

class Node{
public:
    int data;
    Node* next;

    Node(int value){
        data=value;
        next=nullptr;
    }
     
};

int main(){
    Node* first = new Node(10);
    Node* second = new Node(20);
    Node* third = new Node(90);

    first->next=second;
    second->next=third;

    cout << first->next << endl;
    cout << first->next->next<< endl;
    cout << first->next->next->next<< endl;

    return 0;
}
