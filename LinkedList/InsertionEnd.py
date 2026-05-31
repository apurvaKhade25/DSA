class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None

    def insertion_end(self,value):
        New_Node=Node(value)

        if self.head is None:
            self.head=New_Node
        
        temp=self.head

        while temp.next is not None:
            temp=temp.next

        temp.next=New_Node
    
    def print_list(self):
        if not self.head:
            print("Empty list")
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")


ll=LinkList()
# ll.head = Node(10)
# ll.head.next = Node(20)
# ll.head.next.next = Node(30)
# ll.head.next.next.next=Node(40)

n=int(input("Enter no of nodes: "))
values=list(map(int,input("Enter values: ").split()))

ll.head=Node(values[0])
temp=ll.head

for i in range(1,n):
    new_node=Node(values[i])
    temp.next=new_node
    temp=temp.next


print("\nOriginal list")
ll.print_list()

value=int(input("Enter to insert at end: "))
print(f"After insertion of : {value}")
ll.insertion_end(value)
ll.print_list()
            
    

