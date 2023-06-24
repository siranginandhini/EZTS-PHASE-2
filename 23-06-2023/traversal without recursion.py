class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inOrder(root):
    current=root
    stack=[]
    done=0
    while True:
        if current is not None:
            stack.append(current)
            current=current.left
        elif(stack):
            current=stack.pop()
            print(current.data,end=" ")
            current=current.right
        else:
            break
    print()
#INPUT
"""constructed binary tree is

           1
          / \
         2   3
        /\     
       4  5 """
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
inOrder(root)
