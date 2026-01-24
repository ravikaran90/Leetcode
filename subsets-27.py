class Solution:
    def subsets(self,nums):
        def backtrack(start,current_list):
            result.append(current_list[:])
            for i in range(start,len(nums)):
                current_list.append(nums[i])
                backtrack(i+1,current_list)
                current_list.pop()
        result=[]
        backtrack(0,[])
        return result

def main():
    nums=[4,8,12]
    obj=Solution()
    res=obj.subsets(nums)
    print("Top K Frequent:",res)

if __name__=="__main__":
    main()
