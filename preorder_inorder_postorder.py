class Node:
    def __init__(self,val,left=None,right=None):
        self.left=left
        self.val=val
        self.right=right

class Solution:
    def preorder(self,root):
        if root==None:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
    def inorder(self,root):
        if root==None:
            return
        self.preorder(root.left)
        print(root.val)
        self.preorder(root.right)
    def postorder(self,root):
        if root==None:
            return
        self.preorder(root.left)
        self.preorder(root.right)
        print(root.val)

def main():
    root=Node(500)
    root.left=Node(250)
    root.right=Node(400)
    root.left.left=Node(100)
    root.left.right=Node(200)
    root.right.left=Node(300)
    root.right.right=Node(350)
    obj=Solution()
    print("PreOrder:")
    obj.preorder(root)
    print("InOrder:")
    obj.inorder(root)
    print("PostOrder:")
    obj.postorder(root)

if __name__=="__main__":
    main()