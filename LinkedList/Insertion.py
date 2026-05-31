class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkList:
    def __init__(self):
        self.head=None

    def insertBeg(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node

    def print_list(self):
        if not self.head:
            print("List empty")
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

ll = LinkList()

n = int(input("How many nodes? "))

for _ in range(n):

    value = int(input("Enter value: "))

    ll.insertBeg(value)

ll.print_list()

print("WORKING")