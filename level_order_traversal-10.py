from collections import deque

class Node:
    def __init__(self,val,left=None,right=None):
        self.left=left
        self.val=val
        self.right=right

def level_order_traversal(root):
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
    root=Node(60)
    root.left=Node(120)
    root.left.left=Node(240)
    root.left.right=Node(300)
    root.left.left.left=Node(480)
    root.left.left.right=Node(540)
    root.right=Node(45)
    root.right.right=Node(90)
    root.right.left=Node(75)
    root.right.right.left=Node(180)
    root.right.right.right=Node(360)
    res=level_order_traversal(root)
    print("Subsets:",res)

if __name__=="__main__":
    main()