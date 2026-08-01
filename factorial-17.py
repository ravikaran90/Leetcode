def factorial(n):
  if n<1:
    return
  else factorial(n)*factorial(n-1)

def main():
  res=factorial(n)
  print("Factorial:",res)
  

if __name__==__main__:
  main()
