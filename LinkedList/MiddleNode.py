class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_list(self):
        temp=self.head

        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")            

    def middle(self):
        # count=0

        # temp=self.head
        # while temp:
        #     count+= 1
        #     temp=temp.next

        # mid=(count)//2
        # print(mid)
        # temp=self.head
        # for _ in range(mid):
        #     temp=temp.next
        
        # return temp.data

        slow=self.head
        fast=self.head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        return slow.data
    

    
    
ll = LinkedList()
ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next=Node(40)
ll.head.next.next.next.next=Node(90)
ll.print_list()

print(ll.middle())

