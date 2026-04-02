def recursion(n):
    if n<1:
      return 1
    else:
      return recursion(n-1)+recursion(n-2)

def main():
  n=10
  res=recursion(n)

if __name__==__main__:
  main()
