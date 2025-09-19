class Solution:
    def binary_search(self,nums,target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if target==nums[mid]:
                return mid
            elif target<nums[mid]:
                right=mid-1
            elif target>nums[mid]:
                left=mid+1
        return False

def main():
    nums=[10,25,36,48,75,100,150,200,250]
    obj=Solution()
    res=obj.binary_search(nums,200)
    print("Result:",res)

if __name__=="__main__":
    main()
