class Node:
  def __init__(self,val,left=None,right=None):
    self.left=left
    self.val=val
    self.right=right

def bfs(root):
  if root:
    return

def main():
  res=bfs(root)
  print("Result:",res)

if __name__==__main__:
  main()
