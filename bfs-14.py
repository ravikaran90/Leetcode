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
    root=Node(55)
    root.left=Node(100)
    root.left.left=Node(150)
    root.left.right=Node(300)
    root.left.left.left=Node(5000)
    root.left.left.right=Node(10000)
    root.right=Node(200)
    root.right.right=Node(1200)
    root.right.left=Node(600)
    root.right.right.left=Node(20000)
    root.right.right.right=Node(40000)
    obj=Solution()
    res=obj.bfs(root)
    print("Result:",res)

if __name__=="__main__":
    main()