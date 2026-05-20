class node:
    def __init__(self,value):
        self.data=value
        self.next=None


first=node(5)
second=node(10)
third=node(15)

first.next=second
second.next=third

print(first.next,"->")
print(second.data,"->")
print(third.data)

