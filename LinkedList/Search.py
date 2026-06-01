class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    
    def search(self,value):
        temp=self.head
        while temp:
            if value==temp.data:
                return True
            temp=temp.next
        
        return False

ll=LinkedList()
ll.head=Node(10)
ll.head.next=Node(20)
ll.head.next.next=Node(30)
ll.head.next.next.next=Node(40)

print(ll.search(10))
