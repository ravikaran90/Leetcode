def factorial(n):
  if n<0:
    return
  else:
    factorial(n-1)*factorial(n)

def main():
  res=factorial(n)
  print("Result:",res)

if __name__=="__main__":
  main()
