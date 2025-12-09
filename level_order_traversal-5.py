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
    root=Node(104)
    root.left=Node(200)
    root.left.left=Node(90)
    root.left.left.left=Node(72)
    root.left.left.right=Node(36)
    root.left.left.left.left=Node(64)
    root.right=Node(10)
    root.right.right=Node(45)
    root.right.right.right=Node(18)
    root.right.right.left=Node(9)
    root.right.right.right.right=Node(32)
    obj=Solution()
    res=obj.level_order_traversal(root)
    print("Result:",res)

if __name__=="__main__":
    main()