class Solution:
def factorial(n):
  if n<0:
    return
  else:
    return (n-1)*factorai(n)

def main():
  obj=Solution()
  res=obj.factorial(n)
  print("Result:",res)

if __name__=="__main__":
  main()
