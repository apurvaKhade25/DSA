class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def delete_head(self):
        if self.head is None:
            print("head is empty")
            return
        temp=self.head
        self.head=self.head.next
        del temp
        return self.head

    
    def print_list(self):
        temp=self.head

        while temp:
            print(temp.data,end='')
            temp=temp.next
        print('None')

ll = LinkedList()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)

ll.print_list()   # 10 → 20 → 30 → None
ll.delete_head()
ll.print_list()   # 20 → 30 → None


