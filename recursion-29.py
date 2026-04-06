def recursion:
    if n<1:
      return
    else:
      recursion(n-1)+recursion(n-2)
    
def main():
  n=5
  obj=Solution()
  res=obj.recursion(n)
  print("Result:",res)

if __name__==__main__:
  main()
