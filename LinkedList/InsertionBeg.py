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

ll=LinkList()

# ll.head = Node(10)
# ll.head.next = Node(20)
# ll.head.next.next = Node(30)

# print("Original list: ")
# ll.print_list()

# ll.insertBeg(79)
# print("After insertion: ")
# ll.print_list()

n = int(input("Enter number of nodes: "))
values = list(map(int, input("Enter values: ").split()))

# Build initial linked list
ll.head = Node(values[0])
temp = ll.head

for i in range(1, n):
    new_node = Node(values[i])
    temp.next = new_node
    temp = temp.next


print("\nOriginal List:")
ll.print_list()


value = int(input("\nEnter value to insert at beginning: "))

ll.insertBeg(value)

print("\nUpdated List:")
ll.print_list()



