from collections import deque

class Node:
    def __init__(self,val,left=None,right=None):
        self.left=left
        self.val=val
        self.right=right

class Solution:
    def bfs(self,root):
        res=[]
        q=deque()
        q.append(root)

        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

def main():
    root=Node(50)
    root.left=Node(25)
    root.left.left=Node(10)
    root.left.right=Node(30)
    root.right=Node(75)
    root.right.left=Node(70)
    root.right.right=Node(100)
    obj=Solution()
    res=obj.bfs(root)
    print("Result:",res)

if __name__=="__main__":
    main()