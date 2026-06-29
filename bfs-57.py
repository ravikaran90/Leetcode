class Node:
  def __init__(self,val,left=None,right=None):
    self.val=val
    self.left=left
    self.right=right

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
  res=bfs(root)
  

if __name__==__main__:
  main()
