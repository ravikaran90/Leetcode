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
    root=Node(5500)
    root.left=Node(7500)
    root.left.left=Node(10000)
    root.left.right=Node(20000)
    root.left.left.left=Node(25000)
    root.left.left.right=Node(50000)
    root.right=Node(15000)
    root.right.right=Node(80000)
    root.right.left=Node(40000)
    root.right.right.left=Node(100000)
    root.right.right.right=Node(200000)
    obj=Solution()
    result=obj.level_order_traversal(root)
    print("Result:",result)

if __name__=="__main__":
    main()