class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    
class LinkList:
    def __init__(self):
        self.head= None

    
    def mergeLists(list1,list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        arr=[]

        temp=list1
        while temp:
            arr.append(temp.val)
            temp=temp.next
        
        temp=list2
        while temp:
            arr.append(temp.val)
            temp=temp.next
        
        arr.sort()

        head = Node(arr[0])
        tail=head
        for i in range(1,len(arr)):
            new_node=Node(arr[i])
            tail.next=new_node
            tail=tail.next
        return head
    
    def print_list(head):
        temp = head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")

list1=LinkList()
list1 = Node(1)
list1.next = Node(5)
list1.next.next = Node(8)

list2=LinkList()
list2 = Node(2)
list2.next = Node(3)
list2.next.next = Node(4)
list2.next.next.next = Node(10)

result=LinkList.mergeLists(list1,list2)
LinkList.print_list(result)

