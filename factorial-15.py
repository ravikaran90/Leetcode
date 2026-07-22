def factorial(n)
  if n<=0:
    return 0
  else:
    b=factorial(n)*factorial(n-1)

def main():
  n=5
  res=factorial(n)
  print("Result:",res)

if __name__==__main__:
  main()
