from collections import deque

class Node:
    def __init__(self,val,left=None,right=None):
        self.left=left
        self.val=val
        self.right=right

class Solution:
    def btp(self,root):
        if root==None:
            return 0
        else:
            print(root.val)
            leftst = self.btp(root.left)
            print(leftst)
            rightst= self.btp(root.right)
            print(rightst)
            return 1+leftst+rightst

def main():
    root=Node(1)
    root.left=Node(2)
    root.left.left=Node(5)
    root.left.left=Node(8)
    root.left.left.right=Node(7)
    root.right=Node(3)
    obj=Solution()
    res=obj.btp(root)
    print("Result:",res)

if __name__=="__main__":
    main()