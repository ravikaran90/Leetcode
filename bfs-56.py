class Node:
  def __init__(self,val,left=None,right=anone):
    self.val=val
    self.left=left
    self.right=right

def bfs(root):
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
  root=Node(67)
  root.left=Node(100)
  root.right=Node(50)
  root.right.right=Node(150)
  root.right.left=Node(55)
  root.left.left=Node(89)
  root.left.right=Node(120)
  res=bfs(root)
  print("Result:",res)


if __name__==__main__:
  main()
