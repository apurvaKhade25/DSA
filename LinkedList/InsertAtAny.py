class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
    
class LinkList:
    def __init__(self):
        self.head= None

    def InsertAt(self,pos,value):
        new_node=Node(value)

        if pos==1:
            new_node.next=self.head
            self.head=new_node
            return
        
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        
        new_node.next=temp.next
        temp.next=new_node

    
    def print_list(self):
        if not self.head:
            print("List is empty")
        
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print(None)
    
ll = LinkList()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next=Node(40)

ll.print_list()   # 10 → 20 → 30 → None

ll.InsertAt(3,55)
ll.print_list()   # 20 → 30 → None
