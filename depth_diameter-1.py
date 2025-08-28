class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
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
    root=Node(50)
    root.left=Node(25)
    #root.left.left=Node(10)
    #root.left.right=Node(20)
    root.right=Node(80)
    #root.right.right=Node(100)
    #root.right.left=Node(70)
    obj=Solution()
    dep=obj.depth(root)
    print("Depth:",dep)
    dia=obj.diam(root)
    print("Diameter:",dia)

if __name__=="__main__":
    main()