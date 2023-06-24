class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None
    def del_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def del_pos(self):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prv=prev.next
        prev.next=temp.next
        temp.next=None

    def del_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while(temp):
                if temp.next!=None:
                    print(temp.data,"->",end=" ")
                else:
                    print(temp.data,end=" ")
                temp=temp.next
obj=Singlelinkedlist()
n=Node(10)
obj.head=n
n.next=n1
n2=Node(30)
n1.next=
