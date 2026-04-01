def recursion(n):
  if n<0:
    return
  else:
    recursion(n-1)+recursion(n-2)

def main():
  n=10
  res=recursion(n)
  print("Result:",res)

if __name__==__main__:
  main()
