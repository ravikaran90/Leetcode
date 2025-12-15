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
    root.left=Node(7000)
    root.left.left=Node(500)
    root.left.right=Node(1000)
    root.left.left.left=Node(34)
    root.left.left.right=Node(68)
    root.right=Node(14000)
    root.right.right=Node(2000)
    root.right.left=Node(4000)
    root.right.right.left=Node(136)
    root.right.right.right=Node(272)
    obj=Solution()
    res=obj.level_order_traversal(root)
    print("Result:",res)

if __name__=="__main__":
    main()