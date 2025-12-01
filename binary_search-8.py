class Solution:
    def binary_search(self,nums,target):
        left=0
        right=len(nums)
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                right=mid-1
            elif target>nums[mid]:
                left=mid+1
        return False
    
def main():
    nums=[3,6,7,8,11,12,15,18,21,24,27,32]
    obj=Solution()
    res=obj.binary_search(nums,18)
    print("Result:",res)

if __name__=="__main__":
    main()