def recursion(n):
  if n<5:
    return n
  else:
    print(n)
    return recursion(n-1)+recursion(n-2)

def main():
  n=10
  res=recursion(n)

if _name_==__main__:
  main()
