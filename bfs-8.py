from collections import deque

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def bfs(self,root):
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
    root=Node(72)
    root.left=Node(88)
    root.left.left=Node(90)
    root.left.left.left=Node(100)
    root.left.left.right=Node(23)
    root.right=Node(37)
    root.right.right=Node(42)
    root.right.right.left=Node(50)
    root.right.right.right=Node(4)
    obj=Solution()
    res=obj.bfs(root)
    print("Result:",res)

if __name__=="__main__":
    main()