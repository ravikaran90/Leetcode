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
    root=Node(80)
    root.left=Node(600)
    root.right=Node(1200)
    root.left.left=Node(500)
    root.left.right=Node(1000)
    root.right.left=Node(2000)
    root.right.right=Node(4000)
    obj=Solution()
    res=obj.bfs(root)
    print("Result:",res)

if __name__=="__main__":
    main()
