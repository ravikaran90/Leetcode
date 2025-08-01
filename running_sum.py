class Solution: 
    def running_sum(self,nums):
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[len(prefix)-1])
        return prefix

def main():
    nums=[3,1,2,10,1]
    obj=Solution()
    res=obj.running_sum(nums)
    print("Result:",res)

if __name__=="__main__":
    main()