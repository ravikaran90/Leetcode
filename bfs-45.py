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
      node=q.popleft()
      while node:
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
      level.append(q)
    res.append(level)
    
def main():
  root=Node(100)
  obj=Solution()
  res=obj.bfs(root)
  print("Result:",res)

if __name__==__main__:
  main()
