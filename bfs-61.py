from collections import deque

class Node:
  def __init__(self,val,left=None,right=None):
    self.val=val
    self.left=left
    self.right=right

def bfs(root):
  res=[]
  q=deque([root])
  while q:
    level=[]
    node=q.popleft()
    if node.left:
      q.append(node.left)
    if node.right:
      q.append(node.right)
    res.append(level)
  return res

def main():
  res=bfs(root)
  print("BFS:",res)

if __name__==__main__
    main()
