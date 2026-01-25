from collections import deque

class Node:
    def __init__(self,val,left=None,right=None):
        self.left=left
        self.val=val
        self.right=right

class Solution:
    def level_order_traversal(self,root):
        res=[]
        q=deque([root])
        #q.append(root)
        
        while q:
            level=[]
            node=q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            res.append(level)
        return res
    
def main():
    root=Node(22)
    root.left=Node(2000)
    root.right=Node(3000)
    root.left.left=Node(45)
    root.left.right=Node(90)
    root.left.left.left=Node(250)
    root.left.left.right=Node(500)
    root.right.left=Node(800)
    root.right.right=Node(1600)
    obj=Solution()
    res=obj.level_order_traversal(root)
    print("Level Order Traversal:",res)

if __name__=="__main__":
    main()