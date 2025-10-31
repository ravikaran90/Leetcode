from collections import deque

class Node:
    def __init__(self,val,left=None,right=None):
        self.left=None
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
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if level:
                res.append(level)
        return res

def main():
    root=Node(500)
    root.left=Node(250)
    root.left.left=Node(100)
    root.left.right=Node(300)
    root.right=Node(750)
    root.right.right=Node(800)
    root.right.left=Node(650)
    obj=Solution()
    result=obj.bfs(root)
    print("Result:",result)

if __name__=="__main__":
    main()