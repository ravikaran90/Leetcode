class Solution: 
    def sq_sorted_array(self,nums):
        l=0
        r=len(nums)-1
        arr=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[l])>abs(nums[r]):
                sq=nums[l]*nums[l]
                l+=1
            else:
                sq=nums[r]*nums[r]
                r-=1
            arr[i]=sq
        return arr


def main():
    nums=[-4,-1,0,3,10]
    obj=Solution()
    res=obj.sq_sorted_array(nums)
    print("Result:",res)

if __name__=="__main__":
    main()