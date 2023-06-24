#binary tree traversal using recursive function
class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val,end=" ")
        printInorder(root.right)
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val,end=" ")
def printPreorder(root):
    if root:
        print(root.val,end=" ")
        printPreorder(root.left)
        printPreorder(root.right)
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
print("PRE-ORDER:")
printPreorder(root)
print()
print("\n IN-ORDER:")
printInorder(root)
print()
print("\n POST-ORDER")
printPostorder(root)
print()
        
