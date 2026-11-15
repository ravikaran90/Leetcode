def factorial(n):
  if n<0:
    return
  else:
    return n*factorial(n-1)

def main():
  res=factorial(5)
  print("Result:",res)

if __name__=="__main__":
  main()
