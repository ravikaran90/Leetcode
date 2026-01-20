class Solution:
    def move_zeroes(self,nums):
        left=0
        for right in range (len(nums)):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
        return nums

def main():
    nums=[1,4,0,90,2,0,13,0,0,45,98]
    obj=Solution()
    res=obj.move_zeroes(nums)
    print("Result:",res)

if __name__=="__main__":
    main()


