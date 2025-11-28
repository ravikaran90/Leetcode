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
    root=Node(40)
    root.right=Node(32)
    root.right.left=Node(5)
    root.right.right=Node(16)
    root.left=Node(60)
    root.left.left=Node(62)
    root.left.right=Node(34)
    obj=Solution()
    res=obj.level_order_traversal(root)
    print("Result:",res)

if __name__=="__main__":
    main()