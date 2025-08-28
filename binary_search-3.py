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

def main():
    nums=[100,134,146,165,190,250,340,560,600,780,920]
    obj=Solution()
    res=obj.binary_search(nums,560)
    print("Result:",res)

if __name__=="__main__":
    main()