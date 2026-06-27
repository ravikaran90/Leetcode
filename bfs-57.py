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
    node=q.popleft()
    for i in range(q):
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
      level.append(q)
  res.append(level)

def main():
  res=bfs(root)
  

if __name__==__main__:
  main()
