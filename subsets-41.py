class Solution:
  def subsets(self,n):
    def backtrack(start,):
        for i in range(len(n)):
          backtrack(start,current_list)
    
    res=backtrack(0,[])
    print("Result:",res)

def main():
  n=[5,12,15]
  obj=Solution()
  res=obj.subsets(n)
  print("Subsets:",res)

if __name__==__main__:
  main()
