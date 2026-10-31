class fact:
  def factorial(n):
    if n<0:
      return
    else:
      return n*factorial(n-1)

def main():
  obj=fact()
  res=obj.factorial(15)
  print("Result:",res)

if __name__=="__main__":
  main()
