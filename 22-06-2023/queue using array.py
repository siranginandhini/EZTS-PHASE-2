queue=[]
def enqueue():
    element=input("enter the element")
    queue.append(element)
    print(element,"is added in q")
def dequeue():
    if not queue:
        print("q is empty")
    else:
        e=queue.pop(0)
        print("removed element")
def display():
    print(queue)
while True:
    print("select operation 1.add 2.remove 3.display 4.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("pls enter correct operation")
