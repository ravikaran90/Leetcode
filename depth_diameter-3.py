class Node:
    def __init__(self,val,left=None,right=None):
         self.left=left
         self.right=right
         self.val=val

class Solution:
    def depth_diameter(self,root):
        if root==None:
            return 0
        else:
            leftst=self.depth_diameter(root.left)
            rightst=self.depth_diameter(root.right)
            return 1+max(leftst,rightst)
    def diameter(self,root):
         return 1+self.depth_diameter(root.left)+self.depth_diameter(root.right)

def main():
    root=Node(500)
    root.left=Node(200)
    root.left.left=Node(100)
    root.right=Node(700)
    root.right.right=Node(800)
    obj=Solution()
    res=obj.depth_diameter(root)
    print("Result:",res)
    diam=obj.diameter(root)
    print("Diameter:",diam)

if __name__=="__main__":
        main()