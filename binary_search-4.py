class Solution:
    def binary_search(self,nums,target):
        left=0
        right=len(nums)
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                left+=1
            elif target<nums[mid]:
                right-=1
        return False
        

def main():
    nums=[2,5,8,10,12,15,18,20,25,30]
    obj=Solution()
    res=obj.binary_search(nums,30)
    print("Result:",res)

if __name__=="__main__":
    main()