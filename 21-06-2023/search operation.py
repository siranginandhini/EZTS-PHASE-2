class node:
    def _init_(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def _init_(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                if temp.next!=None:
                    print(temp.data,"->",end="")
                else:
                    print(temp.data,end="")
                temp=temp.next
    def search(self,num):
        temp=self.head
        while temp:
            if temp.data==s:
                print("yes!")
                break
            temp=temp.next
        else:
            print("not present")
                
obj=singlelinkedlist()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
obj.display()
s=int(input("\nsearch element:"))
obj.search(s)

