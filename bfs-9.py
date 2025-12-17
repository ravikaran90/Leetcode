from collections import deque

class Node:
    def __init__(self,val,left=None,right=None):
        self.left=left
        self.val=val
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
    root=Node(5)
    root.left=Node(3)
    root.left.left=Node(100)
    root.left.right=Node(50)
    root.left.left.left=Node(360)
    root.left.left.right=Node(180)
    root.right=Node(6)
    root.right.right=Node(25)
    root.right.left=Node(12)
    root.right.right.left=Node(90)
    root.right.right.right=Node(45)
    obj=Solution()
    res=obj.bfs(root)
    print("Result:",res)

if __name__=="__main__":
    main()