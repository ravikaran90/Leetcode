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
    root=Node(60)
    root.left=Node(25)
    root.left.left=Node(28)
    root.left.left.left=Node(2)
    root.left.left.left.left=Node(500)
    root.left.left.left.right=Node(600)
    root.right=Node(50)
    root.right.right=Node(56)
    root.right.right.right=Node(4)
    root.right.right.right.left=Node(800)
    root.right.right.right.right=Node(1000)
    obj=Solution()
    res=obj.level_order_traversal(root)
    print("Result:",res)

if __name__=="__main__":
    main()