class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None

    
    def reverse(self):
        prev=None
        curr=self.head

        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        
        self.head=prev
        
    def print_list(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")
    
ll=LinkedList()

ll.head=Node(10)
ll.head.next=Node(20)
ll.head.next.next=Node(30)
ll.head.next.next.next=Node(40)
ll.reverse()
ll.print_list()
