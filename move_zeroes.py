class Solution: 
    def move_zeroes(self,nums):
        slow=0
        for fast in range(len(nums)):
            if nums[fast]!=0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow+=1
        return nums

def main():
    nums=[0,2,5,0,6,8,3,5,4]
    obj=Solution()
    res=obj.move_zeroes(nums)
    print("Result:",res)

if __name__=="__main__":
    main()