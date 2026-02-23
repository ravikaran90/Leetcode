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
        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
    
def main():
    root=Node(5000)
    root.left=Node(1400)
    root.right=Node(2800)
    root.left.left=Node(250)
    root.left.right=Node(500)
    root.right.left=Node(1000)
    root.right.right=Node(2000)
    obj=Solution()
    res=obj.level_order_traversal(root)
    print("Level Order Traversal:",res)

if __name__=="__main__":
    main()