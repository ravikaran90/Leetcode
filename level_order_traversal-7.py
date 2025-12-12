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
    root=Node(425)
    root.left=Node(750)
    root.left.left=Node(900)
    root.left.right=Node(950)
    root.left.left.left=Node(10000)
    root.left.left.right=Node(5000)
    root.right=Node(375)
    root.right.right=Node(200)
    root.right.left=Node(425)
    root.right.right.left=Node(2500)
    root.right.right.right=Node(1250)
    obj=Solution()
    res=obj.level_order_traversal(root)
    print("Result:",res)

if __name__=="__main__":
    main()