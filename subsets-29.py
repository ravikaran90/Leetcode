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
    obj=Solution()
    nums=[2,3,4,5]
    res=obj.subsets(nums)
    print("Subsets:",res)

if __name__=="__main__": #Running this Python file directly
    main()