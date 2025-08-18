class Solution: 
    def binary_search(self,nums,target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                    return mid
            elif target<nums[mid]:
                 right=mid-1
            elif target>nums[mid]:
                 left=mid+1
        return -1


def main():
    nums=[23,44,66,88,110,122,124,132,145,152,160,180,200]
    obj=Solution()
    res=obj.binary_search(nums,160)
    print("Result:",res)

if __name__=="__main__":
    main()