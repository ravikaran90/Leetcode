class Solution: 
    def binary_search(self,nums,target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(right+left)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                right=mid-1
            elif target>nums[mid]:
                left=mid+1
        return False

def main():
    nums=[10,30,60,80,100,120,250,500,750,800]
    obj=Solution()
    res=obj.binary_search(nums,500)
    print("Result:",res)

if __name__=="__main__":
    main()
