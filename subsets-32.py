import heaps

class Solution:
  def subsets(self,n):
    def backtrack(n,current_list):
      for i in range(n):
        current_list.append(n)

def main():
  n=[56,58,32]
  obj=Solution()
  res=obj.subsets(n)
  print("Subsets:",res)

if __name__==__main__:
  main()
