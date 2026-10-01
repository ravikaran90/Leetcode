def factorial(n):
  if n<1:
    return
  else:
    factorial(n)*factorial(n-1)


def main():
  n=5
  res=factorial(n)
  print("Result:",res)

if __name__==__main__:
  main()
