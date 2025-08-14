class Solution: 
    def binary_search(self,nums,target):
        l=0
        r=len(nums)
        while l<r:
            mid=(l+r)//2
            print(mid)
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                r=mid-1
            elif target>nums[mid]:
                l=mid+1
        return l

def main():
    nums=[10,15,18,22,25,30,40,55,72,90,100]
    obj=Solution()
    res=obj.binary_search(nums,22)
    print("Result:",res)

if __name__=="__main__":
    main()