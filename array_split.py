class Solution: 
    def prefix_sum(self,nums):
        valid_splits=0
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[len(prefix)-1])
        #return prefix
        #[10, 14,  6, 13]
        for i in range(len(prefix)-1):
            left=prefix[i]
            right=prefix[-1]-prefix[i]
            if left>=right:
                valid_splits+=1
            #sum=prefix[i]-prefix[j]+nums[i]
            #if sum>nums:
        return valid_splits
        #First Section has a sum greater than or equal 
        #to the sum of the second section

def main():
    #nums=[2,3,1,0]
    nums=[10,  4, -8,  7]
    #ps-=[10, 14,  6, 13]
    #.   [10][4,-8,7] | [10,4][-8,7] | [10,4,-8][7]

    #[10][10,4,-8][10,4,-8,7]
    obj=Solution()
    res=obj.prefix_sum(nums)
    print("Result:",res)

if __name__=="__main__":
    main()