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

    def diam(self,root):
        return 1+self.depth(root.left)+self.depth(root.right)

def main():
    root=Node(500)
    root.left=Node(300)
    root.left.left=Node(200)
    root.left.right=Node(350)
    root.right=Node(800)
    root.right.left=Node(750)
    root.right.right=Node(1000)
    obj=Solution()
    dp=obj.depth(root)
    print("Depth:",dp)
    diam=obj.diam(root)
    print("Diameter:",diam)

if __name__=="__main__":
    main()
