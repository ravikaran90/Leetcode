class Solution:
  def factorial(n):
    if n<1:
      return
    else factorial(n)*factorial(n-1)

def main():
  obj=Solution()
  res=obj.factorial(n)
  print("Factorial:",res)
  

if __name__==__main__:
  main()
