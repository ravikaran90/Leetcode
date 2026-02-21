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
    root=Node(70)
    root.left=Node(100)
    root.right=Node(200)
    root.left.left=Node(450)
    root.left.right=Node(900)
    root.right.left=Node(1800)
    root.right.right=Node(3600)
    obj=Solution()
    res=obj.level_order_traversal(root)
    print("Level Order Traversal:",res)

if __name__=="__main__":
    main()
