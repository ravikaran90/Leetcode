class Solution:
    def squares_sorted_array(self,nums):
        arr=[0]*len(nums)
        left=0
        right=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[left])<abs(nums[right]):
                sq=nums[right]*nums[right]
                right-=1
            else:
                sq=nums[left]*nums[left]
                left+=1
            arr[i]=sq
        return arr

def main():
    nums=[-4,-1,0,3,10]
    obj=Solution()
    res=obj.squares_sorted_array(nums)
    print("Result:",res)

if __name__=="__main__":
    main()