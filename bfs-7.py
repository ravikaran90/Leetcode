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
    root=Node(30)
    root.left=Node(44)
    root.left.left=Node(55)
    root.left.right=Node(2)
    root.right=Node(23)
    root.right.left=Node(45)
    root.right.right=Node(50)
    obj=Solution()
    res=obj.bfs(root)
    print("Result:",res)

if __name__=="__main__":
    main()