from collections import deque

class Node:
    def __init__(self,val,left=None,right=None):
        self.left=left
        self.val=val
        self.right=right

class Solution:
    def breadth_first_search(self,root):
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
    root=Node(90)
    root.left=Node(150)
    root.right=Node(300)
    root.left.left=Node(4000)
    root.left.right=Node(8000)
    root.right.left=Node(16000)
    root.right.right=Node(32000)
    root.right.right.right=Node(25)
    obj=Solution()
    res=obj.breadth_first_search(root)
    print("Result:",res)

if __name__=="__main__":
    main()

