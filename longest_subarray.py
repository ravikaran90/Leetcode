class Solution:
    def longest_subarrary(self,nums,k):
        left=curr=answer=0
        for right in range(len(nums)):
            curr+=nums[right]
            while curr>k:
                curr-=nums[left]
                left+=1
            answer=max(answer,right-left+1)
        return nums[left:right+1],answer

def main():
    nums=[3,2,1,3,1,1]
    obj=Solution()
    res=obj.longest_subarrary(nums,5)
    print("Longest Subarray and Length:",res)

if __name__=='__main__':
    main()