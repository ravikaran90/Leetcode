class Solution: 
    #Time Complexity: O(n)
    def squares_sorted_array(self,nums):
        left=0
        right=len(nums)-1
        result=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[left])<abs(nums[right]):
                square=nums[right]
                right-=1
            else:
                square=nums[left]
                left+=1
            result[i]=square*square
        return result

    #Time Complexity: O(nlog(n))
    #def squares_sorted_array(self,nums):
    #    for i in range(len(nums)):
    #        nums[i]=nums[i]*nums[i]
    #    nums.sort()
    #    return nums
    
def main():
    nums=[-7,-3,2,3,11]
    obj=Solution()
    res=obj.squares_sorted_array(nums)
    print("Result:",res)

if __name__=="__main__":
    main()