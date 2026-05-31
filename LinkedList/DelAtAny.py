class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def deleteAt(self,pos):
        if self.head is None:
            print("Empty")
        
        if pos==0:
            self.head=self.head.next
            return
        
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        
        temp.next=temp.next.next
    
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")

ll = LinkedList()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next=Node(40)
ll.head.next.next.next.next=Node(90)

ll.print_list()

ll.deleteAt(0)
ll.print_list()