feom collections import deque

class Node:
  def _init_(self,val,left=None,right=None):
    self.left=left
    self.val=val
    self.right=right

class Solution:
  def bfs(self,root):
    res=[]
    q=deque([root])
    
    while q:
      level=[]
      for i in len(q):
        node=q.deque(root)
        if node.left:
          q.append(node.left)
        if node.right:
          q.append(node.right)
      level.append(q)
    res.append(level)

def main():
  root=Node(60)
  root.left=Node(85)
  root.right=Node(125)
  obj=Solution()
  res=obj.bfs(root)
  print("BFS:",res)

if __name__==__main__:
  main()
