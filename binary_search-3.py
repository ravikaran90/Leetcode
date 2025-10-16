class Solution:
    def binary_search(self,nums,target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                left=mid+1
            elif target<nums[mid]:
                right=mid-1
        return -1

def main():
    nums=[7,8,12,15,18,20,22,25,30,43,57,72]
    target=57
    obj=Solution()
    res=obj.binary_search(nums,target)
    print("Number at Position:",res)

if __name__=="__main__":
    main()