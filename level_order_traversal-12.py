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
            node=q.popleft()
            for i in range(len(q)):
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res

def main():
    root=Node(58)
    root.left=Node(89)
    root.right=Node(178)
    root.left.left=Node(150)
    root.left.right=Node(300)
    root.right.left=Node(600)
    root.right.right=Node(1200)
    obj=Solution()
    res=obj.level_order_traversal(root)
    print("Level Order Traversal:",res)

if __name__=="__main__": #Running this Python file directly
    main()