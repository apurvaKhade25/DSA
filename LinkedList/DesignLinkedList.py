class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class MyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0
        

    def get(self, index: int) -> int:
        if index< 0 or index>=self.size:
            return -1
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp.data

    def addAtHead(self, val: int) -> None:
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
        self.size+=1

    def addAtTail(self, val: int) -> None:
        new_node=Node(val)
        if not self.head:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index< 0 or index>self.size:
            return
        if index==0:
            self.addAtHead(val)
            return
        
        new_node=Node(val)
        temp=self.head
        for i in range(index-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
        self.size+=1


    def deleteAtIndex(self, index: int) -> None:
        if index< 0 or index>=self.size:
            return 
        if index==0:
            self.head=self.head.next
        else:
            temp=self.head
            for i in range(index-1):
                temp=temp.next
            temp.next=temp.next.next
        self.size-=1

    
        