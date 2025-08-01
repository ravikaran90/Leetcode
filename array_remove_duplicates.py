class Solution: 
    def remove_duplicates(self,nums):
        unique=1
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                nums[unique]=nums[i]
                unique+=1
        return unique,nums

def main():
    nums=[0,0,1,1,1,2,2,3,3,4]
    obj=Solution()
    res=obj.remove_duplicates(nums)
    print("Result:",res)

if __name__=="__main__":
    main()