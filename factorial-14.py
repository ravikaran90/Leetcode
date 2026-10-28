def factorial(n):
  if n<1:
    return
  else:
    return n*factorial(n-1)

def main():
  res=factorial(n)
  print("Result:",res)

if __name__=="__main__":
  main()
