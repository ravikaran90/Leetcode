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
    nums=[3,6,8,11,14,22,34,42,54,57,62,65]
    obj=Solution()
    res=obj.binary_search(nums,42)
    print("Result:",res)

if __name__=="__main__":
    main()