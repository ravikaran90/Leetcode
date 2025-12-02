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
    root=Node(500)
    root.left=Node(700)
    root.left.left=Node(750)
    root.left.left.left=Node(1000)
    root.left.left.right=Node(650)
    root.right=Node(250)
    root.right.right=Node(200)
    root.right.right.left=Node(645)
    root.right.right.right=Node(620)
    obj=Solution()
    res=obj.level_order_traversal(root)
    print("Result:",res)

if __name__=="__main__":
    main()