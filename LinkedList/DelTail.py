class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None

    def del_tail(self):
        if self.head is None:
            print("No tail to delete")

        if self.head.next is None:
            self.head=None
            return
        
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        
        print(temp.next.next)
        temp.next=None

    
    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data,"-> ",end="")
            temp=temp.next
        print("None")


ll=LinkList()
ll.head=Node(10)
ll.head.next=Node(20)
ll.head.next.next=Node(30)
ll.head.next.next.next=Node(40)

ll.del_tail()
ll.print_list()