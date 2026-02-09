class Solution:
  def subsets(self,nums):
    def bac ktrack(start,current_list):
      result.append(current_list[:])
      for i in range(start,len(nums)):
        current_list.append(nums[i])
        backtrack(i+1,current_list)
        current_list.pop()
    result=[]
    backtrack(0,[])
    return result
  

def main():
  nums=[5,6,7]
  obj=Solution()
  res=obj.subsets(nums)
  print("Subsets:",res)
  
if __name__=="__main__":
  main()
