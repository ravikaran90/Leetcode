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
    nums=[5,10,15,20,25,27,32,38,42,45,50,55,58,62]
    obj=Solution()
    res=obj.binary_search(nums,55)
    print("Result:",res)

if __name__=="__main__":
    main()