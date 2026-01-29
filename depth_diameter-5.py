class Node:
    def __init__(self,val,left=None,right=None):
        self.left=left
        self.val=val
        self.right=right

class Solution:
    def depth(self,root):
        if root==None:
            return 0
        else:
            leftst=self.depth(root.left)
            rightst=self.depth(root.right)
            return 1+max(leftst,rightst)
    def diameter(self,root):
        return 1+self.depth(root.left)+self.depth(root.right)

def main():
    root=Node(50)
    root.left=Node(30)
    root.left.left=Node(20)
    root.left.right=Node(35)
    root.right=Node(80)
    root.right.left=Node(75)
    root.right.right=Node(100)
    obj=Solution()
    res=obj.depth(root)
    print("Depth:",res)
    diam=obj.diameter(root)
    print("Diameter:",diam)

if __name__=="__main__":
    main()