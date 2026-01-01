from collections import deque

class Node:
    def __init__(self,val,left=None,right=None):
        self.left=left
        self.val=val
        self.right=right

class Solution:
    def bfs(self,root):
        result=[]
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
            result.append(level)
        return result

def main():
    root=Node(550)
    root.left=Node(250)
    root.left.left=Node(123)
    root.left.right=Node(246)
    root.left.left.left=Node(155)
    root.left.left.right=Node(310)
    root.right=Node(500)
    root.right.right=Node(492)
    root.right.left=Node(984)
    root.right.right.left=Node(620)
    root.right.right.right=Node(1240)
    obj=Solution()
    res=obj.bfs(root)
    print("Result:",res)

if __name__=="__main__":
    main()