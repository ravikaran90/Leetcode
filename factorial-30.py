def factorial(n):
  if n<1:
    return
  else:
    factorial(n)*factorial(n-1)

def main():
  res=factorial(15)
  print("Result:,res)

if __name---==__main__:
  main()
