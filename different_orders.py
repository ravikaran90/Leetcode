class Node:
    def __init__(self,val,left=None,right=None):
        self.left=left
        self.val=val
        self.right=right

class Solution:
    def preorder(self,root):
        if root==None:
            return None
        else:
            print("Pre Order Traversal:",root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self,root):
        if root==None:
            return None
        else:
            self.inorder(root.left)
            print("In Order Traversal:",root.val)
            self.inorder(root.right)

    def postorder(self,root):
        if root==None:
            return None
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print("Post Order Traversal:",root.val)

def main():
    root=Node(50)
    root.right=Node(75)
    root.left=Node(25)
    obj=Solution()
    obj.preorder(root)
    obj.inorder(root)
    obj.postorder(root)

if __name__=="__main__":
    main()