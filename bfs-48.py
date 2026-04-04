from collections import deque

class Node:
  def __init__(self,val,left=None,right=None):
    self.left=left
    self.val=val
    self.right=right

class Solution:
  def bfs(self,n):
    res=[]
    q=deque([root])
    while q:
      node=node.deque()
      if node.left:
        q.apppend(node.left)
      if node.right:
        q.append(node.right)
      level.append(q)
    res.append(level)

def main():
  root=Node(75)
  root.left=Node(100)
  root.right=Node(125)
  obj=Solution()
  res=obj.bfs(root)
  print("Result:",res)

if __name__==__main__:
  main()
